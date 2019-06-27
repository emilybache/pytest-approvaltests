.. pytest-approvaltests documentation master file, created by
   sphinx-quickstart on Thu Oct  1 00:43:18 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pytest-approvaltests's documentation!
===============================================================

Contents:

.. toctree::
   :maxdepth: 2

See also the documentation for [approval tests](https://github.com/approvals/ApprovalTests.Python)

When your approval tests fail and you are working interactively, you might like
it to open another diff tool than when you are on a CI server for example.

This plugin allows you to configure pytest with which diff tool to use when tests fail.

To set the default reporter to 'PythonNative', suitable for use on the command line:

    pytest --approvaltests-use-reporter='PythonNative'

To define your own diff reporter, perhaps a program with a rich GUI installed only on your developer workstation:

    pytest --approvaltests-add-reporter="diff_program"

The value for 'approvaltests-add-reporter' should be an executable program that can diff two files received as arguments on the command line like this:

    diff_program filepath1 filepath2

if it takes additional arguments, add them with 'approvaltests-add-reporter-args':

    pytest --approvaltests-add-reporter="diff_program" --approvaltests-add-reporter-args="arg1,arg2"

They will be inserted like this:

    diff_program arg1 arg2 filepath1 filepath2

Alternatively you can add these arguments in your pytest.ini file:

[pytest]
addopts = --approvaltests-add-reporter="diff_program"



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

