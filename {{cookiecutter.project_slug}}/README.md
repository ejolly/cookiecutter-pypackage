# {{ cookiecutter.project_name}}  
<!---
[![Build Status](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug | replace("_", "-") }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug | replace("_", "-") }})
[![Package version](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug | replace("_", "-") }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
{% if cookiecutter.documentation == 'rtd' %}
[![Docs](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/index.html)
{% endif %}
--->

{{ cookiecutter.project_short_description }}

## Installation
`pip install git+https://github.com/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}`

{% if cookiecutter.documentation == 'github-pages' %}
    {% if cookiecutter.full_name == 'Eshin Jolly' }
    ## [Documentation](http://eshinjolly.com/{{ cookiecutter.project_slug }}/)
    {% else %}
    ## [Documentation](http://{{ cookiecutter.project_slug }}.github.io/)
    {% endif %}
{% else %}
## [Documentation](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/index.html)

{% endif %}
---------
#### Credit

The scaffold for this package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) with the following [template](https://github.com/ejolly/cookiecutter-pypackage).
