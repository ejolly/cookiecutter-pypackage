# Cookiecutter PyPackage

Itching to get a new Python project up and running *fast*?  
This template will auto-generate a bunch of stuff to make your life super easy!

## Usage

Make sure you have `cookiecutter` installed:  

`pip install cookiecutter`

Then start the project creator using this template:

`cookiecutter https://github.com/ejolly/cookiecutter-pypackage.git`


## See it in action
[![asciicast](https://asciinema.org/a/156036.png)](https://asciinema.org/a/156036)

## Key Features
- Simple [Pypi](https://pypi.python.org/pypi) ready Python package template
- [Sphinx documentation](http://www.sphinx-doc.org/en/stable/) with [auto-doc](http://www.sphinx-doc.org/en/stable/ext/autodoc.html) from docstrings (with examples)
- Multi-environment testing with [tox](https://tox.readthedocs.io/en/latest/) and [pytest](https://docs.pytest.org/en/latest/) (Python 2.7/3.6)
- Quickly [bump version](https://pypi.python.org/pypi/bumpversion/) with single-command
- Hook to auto-publish to pip when pushing new tags to GH
- Basic [travis CI](https://travis-ci.org/) configuration [optional]
- [GH-pages hosted documentation](https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/) in separate branch [optional]
- [Readthedocs](https://readthedocs.org/) hosted documentation compatibility [optional]
- Super useful Make commands:
    - `make install` : local install (editable)
    - `make clean` : remove docs, build, pyc, and test files
    - `make docs` : build documentation
    - `make test`: run multi-environment tests with tox
    - and more...


----
## Credit
This template is a modified fork from the awesome: https://github.com/audreyr/cookiecutter.
