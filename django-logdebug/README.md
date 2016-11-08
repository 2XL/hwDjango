# In software development and product management, a user story is a description consisting of one or more sentences in the everyday or business language of the end user or user of a system that captures what a user does or needs to do as part of his job function.

"who
"what
"why


### Unit Testing

 * it tells a developer that the code is doing things right
 * Testing an individual unit such as a method or function in a class, with all dependencies mocked up



### Functional Testing

 * it tells a developer that the code is doing the right things
 * AKA integration test, testing a slice of functionality in a system, This will test many methods and may interact with dependencies like Databases or WebServices.

### Debugging Django Application


### Logging

 * Django comes with a logging module with the following 5 functions ordered by their severity:
  * debug
  * info
  * warning
  * error
  * critical
 * Logging module is divided into the following four categories
  * Loggers, entry point of the log message of a system, every message written is called a log record, logs contains log levels itself as channels
  * Handlers, decide what to do with the log message, responsible for taking actions for the log record
  * Filters, adds an extra evaluation when a log record is passed from a logger to handler.
  * Formatters, final setp before the message actually gets logged.
  
**Configuration settings.py**
```
# enabling logging setup
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': 'debug.log',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}
```

**Collection views.py**
```
```





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