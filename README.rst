======================
Cookiecutter PyPackage
======================

Simple Cookiecutter template for a Python package forked from https://github.com/audreyr/cookiecutter.

More lightweight with options I typically use.

Features/Differences
--------------------
* Auto :code:`git init`
* Testing with :code:`pytest`
* Testing multiple python versions (major release 2.7-3.6) with :code:`tox`
* Travis-CI: Ready for Travis Continuous Integration testing
* Sphinx_ docs: Documentation ready for generation with ReadTheDocs
* Bumpversion_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master

Usage
-----
Make sure you have :code:`cookiecutter` installed:

.. code-block:: python

    pip install cookiecutter

Then start the project creator using this template:

.. code-block:: python

    cookiecutter https://github.com/ejolly/cookiecutter-pypackage.git
