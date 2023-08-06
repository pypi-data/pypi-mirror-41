# This file is part of Checkbox.
#
# Copyright 2014-2016 Canonical Ltd.
# Written by:
#   Zygmunt Krynicki <zygmunt.krynicki@canonical.com>
#   Maciej Kisielewski <maciej.kisielewski@canonical.com>
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
:mod:`plainbox.impl.launcher` -- launcher definition
==================================================
"""

from gettext import gettext as _
import logging

from plainbox.impl.applogic import PlainBoxConfig
from plainbox.impl.secure import config
from plainbox.impl.session.assistant import SA_RESTARTABLE
from plainbox.impl.session.assistant import get_all_sa_flags
from plainbox.impl.session.assistant import get_known_sa_api_versions
from plainbox.impl.transport import get_all_transports
from plainbox.impl.transport import SECURE_ID_PATTERN


logger = logging.getLogger("plainbox.launcher")


class LauncherDefinition(PlainBoxConfig):
    """
    Launcher definition.

    Launchers are small executables using one of the available user interfaces
    as the interpreter. This class contains all the available options that can
    be set inside the launcher, that will affect the user interface at runtime.
    This generic launcher definition class helps to pick concrete version of
    the launcher definition.
    """
    launcher_version = config.Variable(
        section="launcher",
        help_text=_("Version of launcher to use"))

    config_filename = config.Variable(
        section="config",
        default="checkbox.conf",
        help_text=_("Name of custom configuration file"))

    def get_concrete_launcher(self):
        """Create appropriate LauncherDefinition instance.

        Depending on the value of launcher_version variable appropriate
        LauncherDefinition class is chosen and its instance returned.

        :returns: LauncherDefinition instance
        :raises KeyError: for unknown launcher_version values
        """
        return {'1': LauncherDefinition1}[self.launcher_version]()


class LauncherDefinition1(LauncherDefinition):
    """
    Definition for launchers version 1.

    As specced in https://goo.gl/qJYtPX
    """

    def __init__(self):
        super().__init__()

    launcher_version = config.Variable(
        section="launcher",
        default='1',
        help_text=_("Version of launcher to use"))

    app_id = config.Variable(
        section='launcher',
        default='checkbox-cli',
        help_text=_('Identifier of the application'))

    app_version = config.Variable(
        section='launcher',
        help_text=_('Version of the application'))

    api_flags = config.Variable(
        section='launcher',
        kind=list,
        default=[SA_RESTARTABLE],
        validator_list=[config.SubsetValidator(get_all_sa_flags())],
        help_text=_('List of feature-flags the application requires'))

    api_version = config.Variable(
        section='launcher',
        default='0.99',
        validator_list=[config.ChoiceValidator(
            get_known_sa_api_versions())],
        help_text=_('Version of API the launcher uses'))

    stock_reports = config.Variable(
        section='launcher',
        kind=list,
        validator_list=[
            config.SubsetValidator({
                'text', 'certification', 'certification-staging',
                'submission_files', 'none'}),
            config.OneOrTheOtherValidator(
                {'none'}, {'text', 'certification', 'certification-staging',
                           'submission_files'}),
        ],
        default=['text', 'certification', 'submission_files'],
        help_text=_('List of stock reports to use'))

    local_submission = config.Variable(
        section='launcher',
        kind=bool,
        default=True,
        help_text=_("Send/generate submission report locally when using "
                    "checkbox remote"))

    session_title = config.Variable(
        section='launcher',
        default='session title',
        help_text=_("A title to be applied to the sessions created using "
                    "this launcher that can be used in report generation"))

    session_desc = config.Variable(
        section='launcher',
        default='session description',
        help_text=_("A string that can be applied to sessions created using "
                    "this launcher. Useful for storing some contextual "
                    "infomation about the session"))

    providers = config.Variable(
        section='providers',
        name='use',
        kind=list,
        default=['*'],
        help_text=_('Which providers to load; glob patterns can be used'))

    test_plan_filters = config.Variable(
        section='test plan',
        name='filter',
        default=['*'],
        kind=list,
        help_text=_('Constrain interactive choice to test plans matching this'
                    'glob'))

    test_plan_default_selection = config.Variable(
        section='test plan',
        name='unit',
        help_text=_('Select this test plan by default.'))

    test_plan_forced = config.Variable(
        section='test plan',
        name='forced',
        kind=bool,
        default=False,
        help_text=_("Don't allow the user to change test plan."))

    test_selection_forced = config.Variable(
        section='test selection',
        name='forced',
        kind=bool,
        default=False,
        help_text=_("Don't allow the user to alter test selection."))

    test_exclude = config.Variable(
        section='test selection',
        name='exclude',
        default=[],
        kind=list,
        help_text=_("Exclude test matching the patterns from running"))

    ui_type = config.Variable(
        section='ui',
        name='type',
        default='interactive',
        validator_list=[config.ChoiceValidator(
            ['interactive', 'silent', 'converged', 'converged-silent'])],
        help_text=_('Type of stock user interface to use.'))

    output = config.Variable(
        section='ui',
        default='show',
        validator_list=[config.ChoiceValidator(
            ['show', 'hide', 'hide-resource-and-attachment',
             'hide-automated'])],
        help_text=_('Silence or restrict command output'))

    dont_suppress_output = config.Variable(
        section="ui", kind=bool, default=False,
        help_text=_("Don't suppress the output of certain job plugin types."))

    verbosity = config.Variable(
        section="ui", validator_list=[config.ChoiceValidator(
            ['normal', 'verbose', 'debug'])], help_text=_('Verbosity level'),
        default='normal')

    auto_retry = config.Variable(
        section='ui',
        kind=bool,
        default=False,
        help_text=_("Automatically retry failed jobs at the end"
                    " of the session."))

    max_attempts = config.Variable(
        section='ui',
        kind=int,
        default=3,
        help_text=_("Number of attempts to run a job when in auto-retry mode."))

    delay_before_retry = config.Variable(
        section='ui',
        kind=int,
        default=1,
        help_text=_("Delay (in seconds) before retrying failed jobs in"
                    " auto-retry mode."))

    normal_user = config.Variable(
        section='daemon',
        kind=str,
        default='',
        help_text=_("Username to use for jobs that don't specify user"))

    restart_strategy = config.Variable(
        section='restart',
        name='strategy',
        help_text=_('Use alternative restart strategy'))

    restart = config.Section(
        help_text=_('Restart strategy parameters'))

    reports = config.ParametricSection(
        name='report',
        help_text=_('Report declaration'))

    exporters = config.ParametricSection(
        name='exporter',
        help_text=_('Exporter declaration'))

    transports = config.ParametricSection(
        name='transport',
        help_text=_('Transport declaration'))

    environment = config.Section(
        help_text=_('Environment variables to use'))

    daemon = config.Section(
        name='daemon',
        help_text=_('Daemon-specific configuration'))


DefaultLauncherDefinition = LauncherDefinition1
