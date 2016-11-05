

[pytest-doc](https://pytest-django.readthedocs.io/en/latest/)


Feature: 
 * Less builerplate: no need to import unnittest, create a subclass with methods. Just write tests as regular functions
 * Manage test dependencies with fixtures
 * Database re-use: no need to re-create the test database for every test run.
 * Run tests in multiple processos for increasing speed
 * There are a lot of other nice plugins available for pytest
 * Easy switching: Existing unittest-style tests will work without any modifications.
 

 
Install: 
```
pip install pytest-django
# define DJANGO_SETTINGS_MODULE

# create "<project_root>/pytest.ini"

[pytest]
DJANGO_SETTINGS_MODULE=<project_name>.settings

# to run the test, [load test settings from cli has higher priority]
pytest [--ds=test_settings]


```


Usage:
```
# run suite of test:
pytest

# run specific files or directories 
pytest test_<test_name>.py <test_directory>


# running tests in parallel with pytest-xdist plugin
pip install pytest-xdist 
pytest -n <number of processes>

```


Test Lookup:
By default, pytest looks for tests in the files named test_*
for test files with other names, they will not be collected
















Issues and FAQ 
 * [Tests not found??](https://pytest-django.readthedocs.io/en/latest/faq.html#faq-tests-not-being-picked-up)










[Reusable Apps](https://docs.djangoproject.com/en/1.10/intro/reusable-apps/)


```
# Django App skeleton

    polls/
        admin.py
        __init__.py
        models.py
        templates/
            polls/
                detail.html
                index.html
                results.html
        tests.py
        urls.py
        views.py


# generate the dist directory and builds a new django package.

python setup.py sdist # run from inside django-<appname>

# install

pip install --user django-<appname>/dist/django-<appname>-x.x.tar.gz

# uninstall

pip uninstall django-<appname>

# publish the package on a public repo. [https://pypi.python.org/pypi]
# how to publish https://packaging.python.org/

```