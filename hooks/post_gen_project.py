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
    subprocess.call("git commit -m 'Initial project creation.'",shell=True)

if __name__ == '__main__':
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    git_init()
