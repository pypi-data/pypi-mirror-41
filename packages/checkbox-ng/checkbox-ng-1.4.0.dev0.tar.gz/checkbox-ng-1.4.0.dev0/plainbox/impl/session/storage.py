# This file is part of Checkbox.
#
# Copyright 2012, 2013 Canonical Ltd.
# Written by:
#   Zygmunt Krynicki <zygmunt.krynicki@canonical.com>
#
# Checkbox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3,
# as published by the Free Software Foundation.

#
# Checkbox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Checkbox.  If not, see <http://www.gnu.org/licenses/>.

"""
:mod:`plainbox.impl.session.storage` -- storage for sessions
============================================================

This module contains storage support code for handling sessions. Using the
:class:`SessionStorageRepository` one can enumerate sessions at a particular
location. Each location is wrapped by a :class:`SessionStorage` instance. That
latter class be used to create (allocate) and remove all of the files
associated with a particular session.
"""

import datetime
import errno
import logging
import os
import shutil
import stat
import sys
import tempfile

from plainbox.i18n import gettext as _, ngettext
from plainbox.impl.runner import slugify

logger = logging.getLogger("plainbox.session.storage")


class SessionStorageRepository:
    """
    Helper class to enumerate filesystem artefacts of current or past Sessions

    This class collaborates with :class:`SessionStorage`. The basic
    use-case is to open a well-known location and enumerate all the sessions
    that are stored there. This allows to create :class:`SessionStorage`
    instances to further manage each session (such as remove them by calling
    :meth:SessionStorage.remove()`)
    """

    def __init__(self, location=None):
        """
        Initialize new repository at the specified location.

        The location does not have to be an existing directory. It will be
        created on demand. Typically it should be instantiated with the default
        location.
        """
        if location is None:
            location = self.get_default_location()
        self._location = location

    @property
    def location(self):
        """
        pathname of the repository
        """
        return self._location

    def get_storage_list(self):
        """
        Enumerate stored sessions in the repository.

        If the repository directory is not present then an empty list is
        returned.

        :returns:
            list of :class:`SessionStorage` representing discovered sessions
            sorted by their age (youngest first)
        """
        logger.debug(_("Enumerating sessions in %s"), self._location)
        try:
            # Try to enumerate the directory
            item_list = sorted(os.listdir(self._location),
                key=lambda x: os.stat(os.path.join(
                    self._location, x)).st_mtime, reverse=True)
        except OSError as exc:
            # If the directory does not exist,
            # silently return empty collection
            if exc.errno == errno.ENOENT:
                return []
            # Don't silence any other errors
            raise
        session_list = []
        # Check each item by looking for directories
        for item in item_list:
            pathname = os.path.join(self.location, item)
            # Make sure not to follow any symlinks here
            stat_result = os.lstat(pathname)
            # Consider non-hidden directories that end with the word .session
            if (not item.startswith(".") and item.endswith(".session")
                    and stat.S_ISDIR(stat_result.st_mode)):
                logger.debug(_("Found possible session in %r"), pathname)
                session = SessionStorage(pathname)
                session_list.append(session)
        # Return the full list
        return session_list

    def __iter__(self):
        """
        Same as :meth:`get_storage_list()`
        """
        return iter(self.get_storage_list())

    @classmethod
    def get_default_location(cls):
        """
        Get the default location of the session state repository

        The default location is defined by ``$PLAINBOX_SESSION_REPOSITORY``
        which must be a writable directory (created if needed) where plainbox
        will keep its session data. The default location, if the environment
        variable is not provided, is
        ``${XDG_CACHE_HOME:-$HOME/.cache}/plainbox/sessions``
        """
        repo_dir = os.environ.get('PLAINBOX_SESSION_REPOSITORY')
        if repo_dir is not None:
            repo_dir = os.path.abspath(repo_dir)
        else:
            # Pick XDG_CACHE_HOME from environment
            xdg_cache_home = os.environ.get('XDG_CACHE_HOME')
            # If not set or empty use the default ~/.cache/
            if not xdg_cache_home:
                xdg_cache_home = os.path.join(
                    os.path.expanduser('~'), '.cache')
            # Use a directory relative to XDG_CACHE_HOME
            repo_dir = os.path.join(xdg_cache_home, 'plainbox', 'sessions')
        if (repo_dir is not None and os.path.exists(repo_dir)
                and not os.path.isdir(repo_dir)):
            logger.warning(
                _("Session repository %s it not a directory"), repo_dir)
            repo_dir = None
        if (repo_dir is not None and os.path.exists(repo_dir)
                and not os.access(repo_dir, os.W_OK)):
            logger.warning(
                _("Session repository %s is read-only"), repo_dir)
            repo_dir = None
        if repo_dir is None:
            repo_dir = tempfile.mkdtemp()
            logger.warning(
                _("Using temporary directory %s as session repository"),
                repo_dir)
        return repo_dir


class LockedStorageError(IOError):
    """
    Exception raised when SessionStorage.save_checkpoint() finds an existing
    'next' file from a (presumably) previous call to save_checkpoint() that
    got interrupted
    """


class SessionStorage:
    """
    Abstraction for storage area that is used by :class:`SessionState` to
    keep some persistent and volatile data.

    This class implements functions performing input/output operations
    on session checkpoint data. The location property can be used for keeping
    any additional files or directories but keep in mind that they will
    be removed by :meth:`SessionStorage.remove()`

    This class indirectly collaborates with :class:`SessionSuspendHelper` and
    :class:`SessionResumeHelper`.
    """

    _SESSION_FILE = 'session'

    _SESSION_FILE_NEXT = 'session.next'

    def __init__(self, location):
        """
        Initialize a :class:`SessionStorage` with the given location.

        The location is not created. If you want to ensure that it exists
        call :meth:`create()` instead.
        """
        self._location = location

    def __repr__(self):
        return "<{} location:{!r}>".format(
            self.__class__.__name__, self.location)

    @property
    def location(self):
        """
        location of the session storage
        """
        return self._location

    @property
    def id(self):
        """
        identifier of the session storage (name of the random directory)
        """
        return os.path.splitext(os.path.basename(self.location))[0]

    @property
    def session_file(self):
        """
        pathname of the session state file
        """
        return os.path.join(self._location, self._SESSION_FILE)

    @classmethod
    def create(cls, base_dir, prefix='pbox-'):
        """
        Create a new :class:`SessionStorage` in a random subdirectory
        of the specified base directory. The base directory is also
        created if necessary.

        :param base_dir:
            Directory in which a random session directory will be created.
            Typically the base directory should be obtained from
            :meth:`SessionStorageRepository.get_default_location()`

        :param prefix:
            String which should prefix all session filenames. The prefix is
            sluggified before use.
        """
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        isoformat = "%Y-%m-%dT%H.%M.%S"
        timestamp = datetime.datetime.utcnow().strftime(isoformat)
        location = os.path.join(base_dir, "{prefix}{timestamp}{suffix}".format(
            prefix=slugify(prefix), timestamp=timestamp, suffix='.session'))
        uniq = 1
        while os.path.exists(location):
            location = os.path.join(
                base_dir, "{prefix}{timestamp}_({uniq}){suffix}".format(
                    prefix=slugify(prefix), timestamp=timestamp,
                    uniq=uniq, suffix='.session'))
            uniq += 1
        os.mkdir(location)
        logger.debug(_("Created new storage in %r"), location)
        self = cls(location)
        return self

    def remove(self):
        """
        Remove all filesystem entries associated with this instance.
        """
        logger.debug(_("Removing session storage from %r"), self._location)
        def error_handler(function, path, excinfo):
            logger.warning(_("Cannot remove %s"), path)
        shutil.rmtree(self._location, onerror=error_handler)

    def load_checkpoint(self):
        """
        Load checkpoint data from the filesystem

        :returns: data from the most recent checkpoint
        :rtype: bytes

        :raises IOError, OSError:
            on various problems related to accessing the filesystem
        """
        # Open the location directory
        location_fd = os.open(self._location, os.O_DIRECTORY)
        try:
            # Open the current session file in the location directory
            session_fd = os.open(
                self._SESSION_FILE, os.O_RDONLY, dir_fd=location_fd)
            # Stat the file to know how much to read
            session_stat = os.fstat(session_fd)
            try:
                # Read session data
                data = os.read(session_fd, session_stat.st_size)
                if len(data) != session_stat.st_size:
                    raise IOError(_("partial read?"))
            finally:
                # Close the session file
                os.close(session_fd)
        except IOError as exc:
            if exc.errno == errno.ENOENT:
                # Treat lack of 'session' file as an empty file
                return b''
            raise
        else:
            return data
        finally:
            # Close the location directory
            os.close(location_fd)

    def save_checkpoint(self, data):
        """
        Save checkpoint data to the filesystem.

        The directory associated with this :class:`SessionStorage` must already
        exist. Typically the instance should be obtained by calling
        :meth:`SessionStorage.create()` which will ensure that this is already
        the case.

        :raises TypeError:
            if data is not a bytes object.

        :raises LockedStorageError:
            if leftovers from previous save_checkpoint() have been detected.
            Normally those should never be here but in certain cases that is
            possible. Callers might want to call :meth:`break_lock()`
            to resolve the problem and try again.

        :raises IOError, OSError:
            on various problems related to accessing the filesystem.
            Typically permission errors may be reported here.
        """
        if not isinstance(data, bytes):
            raise TypeError("data must be bytes")
        logger.debug(ngettext(
            "Saving %d byte of data (%s)",
            "Saving %d bytes of data (%s)",
            len(data)), len(data), "UNIX, python 3.3 or newer")
        # Open the location directory, we need to fsync that later
        # XXX: this may fail, maybe we should keep the fd open all the time?
        location_fd = os.open(self._location, os.O_DIRECTORY)
        logger.debug(
            _("Opened %r as descriptor %d"), self._location, location_fd)
        try:
            # Open the "next" file in the location_directory
            #
            # Use openat(2) to ensure we always open a file relative to the
            # directory we already opened above. This is essential for fsync(2)
            # calls made below.
            #
            # Use "write" + "create" + "exclusive" flags so that no race
            # condition is possible.
            #
            # This will never return -1, it throws IOError when anything is
            # wrong. The caller has to catch this.
            #
            # As a special exception, this code handles EEXISTS
            # (FIleExistsError) and converts that to LockedStorageError
            # that can be especially handled by some layer above.
            try:
                next_session_fd = os.open(
                    self._SESSION_FILE_NEXT,
                    os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644,
                    dir_fd=location_fd)
            except FileExistsError:
                raise LockedStorageError()
            logger.debug(
                _("Opened next session file %s as descriptor %d"),
                self._SESSION_FILE_NEXT, next_session_fd)
            try:
                # Write session data to disk
                #
                # I cannot find conclusive evidence but it seems that
                # os.write() handles partial writes internally. In case we do
                # get a partial write _or_ we run out of disk space, raise an
                # explicit IOError.
                num_written = os.write(next_session_fd, data)
                logger.debug(ngettext(
                    "Wrote %d byte of data to descriptor %d",
                    "Wrote %d bytes of data to descriptor %d", num_written),
                    num_written, next_session_fd)
                if num_written != len(data):
                    raise IOError(_("partial write?"))
            except Exception as exc:
                logger.warning(_("Unable to complete write: %r"), exc)
                # If anything goes wrong we should unlink the next file. As
                # with the open() call above we use unlinkat to prevent race
                # conditions.
                # TRANSLATORS: unlinking as in deleting a file
                logger.warning(_("Unlinking %r"), self._SESSION_FILE_NEXT)
                os.unlink(self._SESSION_FILE_NEXT, dir_fd=location_fd)
            else:
                # If the write was successful we must flush kernel buffers.
                #
                # We want to be sure this data is really on disk by now as we
                # may crash the machine soon after this method exits.
                logger.debug(
                    # TRANSLATORS: please don't translate fsync()
                    _("Calling fsync() on descriptor %d"), next_session_fd)
                try:
                    os.fsync(next_session_fd)
                except OSError as exc:
                    logger.warning(_("Cannot synchronize file %r: %s"),
                                   self._SESSION_FILE_NEXT, exc)
            finally:
                # Close the new session file
                logger.debug(_("Closing descriptor %d"), next_session_fd)
                os.close(next_session_fd)
            # Rename FILE_NEXT over FILE.
            #
            # Use renameat(2) to ensure that there is no race condition if the
            # location (directory) is being moved
            logger.debug(
                _("Renaming %r to %r"),
                self._SESSION_FILE_NEXT, self._SESSION_FILE)
            try:
                os.rename(self._SESSION_FILE_NEXT, self._SESSION_FILE,
                          src_dir_fd=location_fd, dst_dir_fd=location_fd)
            except Exception as exc:
                # Same as above, if we fail we need to unlink the next file
                # otherwise any other attempts will not be able to open() it
                # with O_EXCL flag.
                logger.warning(
                    _("Unable to rename/overwrite %r to %r: %r"),
                    self._SESSION_FILE_NEXT, self._SESSION_FILE, exc)
                # TRANSLATORS: unlinking as in deleting a file
                logger.warning(_("Unlinking %r"), self._SESSION_FILE_NEXT)
                os.unlink(self._SESSION_FILE_NEXT, dir_fd=location_fd)
            # Flush kernel buffers on the directory.
            #
            # This should ensure the rename operation is really on disk by now.
            # As noted above, this is essential for being able to survive
            # system crash immediately after exiting this method.

            # TRANSLATORS: please don't translate fsync()
            logger.debug(_("Calling fsync() on descriptor %d"), location_fd)
            try:
                os.fsync(location_fd)
            except OSError as exc:
                logger.warning(_("Cannot synchronize directory %r: %s"),
                               self._location, exc)
        finally:
            # Close the location directory
            logger.debug(_("Closing descriptor %d"), location_fd)
            os.close(location_fd)

    def break_lock(self):
        """
        Forcibly unlock the storage by removing a file created during
        atomic filesystem operations of save_checkpoint().

        This method might be useful if save_checkpoint()
        raises LockedStorageError. It removes the "next" file that is used
        for atomic rename.
        """
        _next_session_pathname = os.path.join(
            self._location, self._SESSION_FILE_NEXT)
        logger.debug(
            # TRANSLATORS: unlinking as in deleting a file
            # Please keep the 'next' string untranslated
            _("Forcibly unlinking 'next' file %r"), _next_session_pathname)
        os.unlink(_next_session_pathname)
