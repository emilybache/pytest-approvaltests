====================
pytest-approvaltests
====================

.. image:: https://img.shields.io/pypi/v/pytest-approvaltests.svg
    :target: https://pypi.org/project/pytest-approvaltests
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-approvaltests.svg
    :target: https://pypi.org/project/pytest-approvaltests
    :alt: Python versions

.. image:: https://travis-ci.org/emilybache/pytest-approvaltests.svg?branch=master
    :target: https://travis-ci.org/emilybache/pytest-approvaltests
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/emilybache/pytest-approvaltests?branch=master
    :target: https://ci.appveyor.com/project/emilybache/pytest-approvaltests/branch/master
    :alt: See Build Status on AppVeyor

A plugin to use approvaltests with pytest

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


Features
--------

Configure approvaltests for use with pytest.
   - indicate which of the reporters to use on test failure
   - define your own diff reporter to use on test failure


Requirements
------------

approvaltests


Installation
------------

You can install "pytest-approvaltests" via `pip`_ from `PyPI`_::

    $ pip install pytest-approvaltests


Usage
-----

See also the documentation for `approval tests <https://github.com/approvals/ApprovalTests.Python>`_

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



Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-approvaltests" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/emilybache/pytest-approvaltests/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
