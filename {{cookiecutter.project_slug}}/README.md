# {{ cookiecutter.project_name}}  
<!---
[![Build Status](https://travis-ci.org/ejolly/{{ cookiecutter.project_slug | replace("_", "-") }}.svg?branch=master)](https://travis-ci.org/ejolly/{{ cookiecutter.project_slug | replace("_", "-") }})
[![Package version](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug | replace("_", "-") }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
{% if cookiecutter.documentation == 'rtd' %}
[![Docs](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/index.html)
{% endif %}
--->

{{ cookiecutter.project_short_description }}

## Installation
`pip install git+https://github.com/ejolly/{{ cookiecutter.project_slug }}`

{% if cookiecutter.documentation == 'gh' %}
## [Documentation](http://eshinjolly.com/{{ cookiecutter.project_slug }}/)
{% else %}
## [Documentation](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/index.html)

{% endif %}
---------
#### Credit

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) with the following [template](https://github.com/ejolly/cookiecutter-pypackage).
http://eshinjolly.com/pybest/
