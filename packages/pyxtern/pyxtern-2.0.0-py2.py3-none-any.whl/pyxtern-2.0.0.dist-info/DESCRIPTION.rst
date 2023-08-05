=======
pyxtern
=======

This package provides decorators and methods to run any external command line in a proper maner. It allows the creation of any command line python interface with ease.

How to install
==============

Since **pyxtern** is hosted on `PyPI <https://pypi.org/project/pyxtern/>`_, it can be installed using:

.. code-block:: shell

        pip install pyxtern

How to use
==========

The full documentation is available `here <https://mar-grignard.gitlab.io/pyxtern>`_.
The following example presents the simplest way of using **pyxtern**:

.. code-block:: python

        from pyxtern import run

        cmd = "find ./pyxtern -name *.py"
        exit, out, err = run(cmd.split(), tee=True)


