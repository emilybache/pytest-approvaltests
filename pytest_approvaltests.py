# -*- coding: utf-8 -*-

import approvaltests
from approvaltests.reporters import GenericDiffReporterFactory


def pytest_addoption(parser):
    """Add options to configure approval testing."""
    group = parser.getgroup('approvaltests', 'approval testing')
    group.addoption('--approvaltests-use-reporter', action='store', metavar='REPORTER',
                    nargs='?', const=True, dest='approvaltests_reporter',
                    help='Named difference reporter to use when approval tests fail '
                         'For example ClipboardReporter or PythonNative.')
    group.addoption('--approvaltests-add-reporter', action='store', metavar='CUSTOM_REPORTER',
                    nargs='?', const=True, dest='approvaltests_custom_reporter',
                    help='Add a custom reporter to use when approval tests fail.'
                    'This should be the path to an executable program that can diff two files passed as arguments')
    group.addoption('--approvaltests-add-reporter-args', action='store', metavar='CUSTOM_REPORTER_ARGS',
                    nargs='?', const=True, dest='approvaltests_custom_reporter_args',
                    help='Add arguments to a custom reporter to use when approval tests fail.'
                         'This should only be used together with the option approvaltests-add-reporter'
                         'It specifies additional arguments to pass to the executable program that can diff files')


def pytest_configure(config):
    factory = GenericDiffReporterFactory()

    custom_reporter = config.option.approvaltests_custom_reporter
    if custom_reporter:
        args = get_reporter_args(config.option.approvaltests_custom_reporter_args)
        reporter = create_reporter(factory, custom_reporter, args)
    else:
        reporter = factory.get(config.option.approvaltests_reporter)

    approvaltests.set_default_reporter(reporter)


def get_reporter_args(args_str):
    if args_str:
        args = args_str.split(',')
    else:
        args = []
    return args


def create_reporter(factory, custom_reporter, args):
    reporter_name = "Custom"
    reporter_config = [reporter_name,
                       custom_reporter,
                       args]
    factory.add_default_reporter_config(reporter_config)
    reporter = factory.get(reporter_name)
    return reporter



