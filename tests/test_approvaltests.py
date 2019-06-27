# -*- coding: utf-8 -*-
import os


def test_approvaltests_use_reporter(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module with a failing approval test
    testdir.makepyfile("""
        from approvaltests import verify
        def test_sth():
            verify("foo")
    """)

    # run pytest with approvaltests configuration to use the PythonNative diff tool
    result = testdir.runpytest(
        '--approvaltests-use-reporter=PythonNative',
        '-v'
    )

    # assert the test fails
    # and these lines 'to approve this result' are produced by the PythonNative reporter
    result.stdout.fnmatch_lines([
        '*::test_sth FAILED*',
        '*to approve this result:*'
    ])


def test_approvaltests_add_reporter(testdir, tmpdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module with a failing approval test
    testdir.makepyfile("""
        from approvaltests import verify
        def test_sth():
            verify("foo")
    """)
    # create a diff tool that just prints 'diff program is executing'
    diff_program_contents = "print('diff program is executing')"
    diff_tool = os.path.join(tmpdir, "diff.py")
    with open(diff_tool, "w") as f:
        f.write(diff_program_contents)

    # run pytest with configuration for custom diff tool
    result = testdir.runpytest(
        '--approvaltests-add-reporter=python',
        '--approvaltests-add-reporter-args=' + str(diff_tool),
        '-v'
    )

    # assert that the diff program did execute on the test failure
    result.stdout.fnmatch_lines([
        '*::test_sth FAILED*',
        '*diff program is executing*'
    ])


def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # assert the help text includes information about the
    # approvaltests options
    result.stdout.fnmatch_lines([
        'approval testing:',
        '*--approvaltests-use-reporter=*',
        '*--approvaltests-add-reporter=*',
        '*--approvaltests-add-reporter-args=*',
    ])
