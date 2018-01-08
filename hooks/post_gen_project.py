#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def git_init():
    os.chdir(PROJECT_DIRECTORY)
    subprocess.call("git init",shell=True)
    subprocess.call("git add .",shell=True)
    subprocess.call("git commit --quiet -m 'Initial project creation.'",shell=True)
    subprocess.call("make -C docs html-quiet",shell=True)
    {% if cookiecutter.documentation == 'github-pages' %}
    subprocess.call("git checkout --orphan gh-pages",shell=True)
    subprocess.call("git reset --hard",shell=True)
    subprocess.call("cp -r docs/_build/html/ .", shell=True)
    subprocess.call("echo 'docs/*' > .gitignore", shell=True)
    subprocess.call("echo '{{ cookiecutter.project_slug }}/' >> .gitignore", shell=True)
    subprocess.call("git add -A",shell=True)
    subprocess.call("git commit --quiet -m 'Initial docs creation.'", shell=True)
    subprocess.call("git checkout master",shell=True)
    {% endif %}

def user_note():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nSuccessfully created {{ cookiecutter.project_name }}!")
    print("Here's what I did:")
    print("1) Created a Python project ready to be deployed with pypi")
    print("2) Committed that project to a new git repo.")
    print("3) Created basic documentation using Sphinx")
    print("4) Setup Python 2 and 3 testing using tox")

    {% if cookiecutter.use_pypi_deployment_with_travis == 'y' %}
    print("5) Setup basic travis CI configuration (you need to edit+run travis_pypi_setup.py to complete this process)")
    {% endif %}

    {% if cookiecutter.documentation == 'github-pages' %}
    print("6) Setup your documentation for compatibility with Github pages using a separate gh-pages branch.\n   Just push that branch to GH to see live documentation at {{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}\n")
    {% else %}
    print("6) Setup your documentation for compatiblity with readthedocs\n")
    {% endif %}

    print("Here are some files you probably want to modify:\n")
    print("DOCS:")
    print("docs/index.rst - to adjust main docs page")
    print("docs/usage.rst - to adjust usage docs page")
    print("docs/api.rst - to adjust what code gets auto-doc'd")
    print("docs/conf.py - to adjust sphinx settings (e.g. mock modules)")
    print("README.md - to adjust project description and badges\n")
    print("SOURCE:")
    print("{{ cookiecutter.project_slug }}/__init__.py - module imports")
    print("setup.py - for tags on different Python versions")
    print("requirements.txt - for added dependencies\n")
    print("TESTS:")
    print("tox.ini - to fine-tune testing environment")
    print("travis_pypi_setup.py - to fine-tune travis CI setup")
    print("A handy feature you get with this cookiecutter is a list of shortcut commands to do common things.")
    print("Just type 'make cmd' using any of the cmd below in your project root (i.e. {{ cookiecutter.project_slug }}/) to use them:\n")
    subprocess.call("cd {{ cookiecutter.project_slug}}",shell=True)
    subprocess.call("make",shell=True)


if __name__ == '__main__':
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    git_init()
    user_note()
