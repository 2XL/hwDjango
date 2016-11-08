### Unit Testing

 * it tells a developer that the code is doing things right
 * Testing an individual unit such as a method or function in a class, with all dependencies mocked up



### Functional Testing

 * it tells a developer that the code is doing the right things
 * AKA integration test, testing a slice of functionality in a system, This will test many methods and may interact with dependencies like Databases or WebServices.
    * also know as Black-Box tests
    * also know as Acceptance tests
    * User story as comments
    * switch to unittest
 
#### Key Concepts:
 * User story: A description of how the application will work form the point of view of the usr.
    Used to structure a function test.
 * Expected failure: When a test fails in a way that we expected it to.

```python

# run functional tests
python functional_tests.py

# run unit tests
python manage.py test <appname>

# code cycle
    # run the test
    # make minimal change
    # repeat

# refactoring
    # when we try to improve the code without changing its functionality
    # its a good idea to do a commit after any refactoring
```

```
Idiomatic term | Django term | Meaning
Model          | Model       | Contains all the business logic. At the very least the database access logic
View           | Template    | Responsible for generating the HTML and other UI
Controller     | View        | Contains the logic to tie the other parts together and to generate a response to a user request
``` 
 

[Reusable Apps](https://docs.djangoproject.com/en/1.10/intro/reusable-apps/)



# Obay the Testing Goat: Do nothing until you have a test
```
functional_test.py

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title


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