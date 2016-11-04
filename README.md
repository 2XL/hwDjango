##### TODO list

* [ ] django
* [ ] django creating view, model and Controller

* [ ] django-apps
* [ ] django-middleware

* [ ] django-orm
* [ ] django-rest
* [ ] django-reusable-apps

##### Installing Django

```
sudo apt-get install python-django

python -c "import django; print django.__version__" # django-admin.py --version

```



##### Django env vars

* export DJANGO_COLORS="{dark,light,ncolor}"


##### Django admin && manage.py [ref](https://docs.djangoproject.com/en/1.10/ref/django-admin/)

```

## Django-admin: idea of separation between content publishers and public site
# 

python manage.py createsuperuser

>prompted: <username>
>prompted: <email>
>prompted: <password>

## Django-admin section URL:
 
> http://<domain>:<port>/admin/


## Django admin commands, they are equivalent...
django-admin <command> [opts]
manage.py <command> [opts]
python -m django <command> [opts]


# --verbosity|-v {0,1,2,3} => no, normal, verbose, very_verbose 

```


##### Useful Commands


```
## create django project

django-admin startproject <project_name>

django_bookmarks/
|-- django_bookmarks
| |-- __init__.py       # django projects are python packages <collection of modules>
| |-- settings.py       # specify configuration and setup features. <database, middleware, apps...>
| |-- urls.py           # mapping between url and python functions 
| `-- wsgi.py
`-- manage.py           # utility script used to manage the project


## creating database tables

python manage.py syncdb

## start the server

python manage.py runserver [[<ip>:]<port number>]

python manage.py runserver 8080             # only visible to dev host
python manage.py runserver 0.0.0.0:8000     # visible to any host within dev host range

## Django CLI shell

python manage.py shell

# Query MODEL API

> from <appName>.models import <modelClass>
> <modelClass>.objects.all()
> modelInstance = <modelClass>([<key>=<value>][,...])
> modelInstance.save()
> modelInstance.id
> <modelClass>.objects.get(<attribute>=<value>)
> modelInstance.<fkClassName>_set.<querySelector>() # querySelector : [all|count|create]
> dir(<className>) # we can see that Django generates <fk_Classname>_set function
> <className



```

##### Django M[V](https://docs.djangoproject.com/en/1.10/intro/tutorial04/)C

```

### Models

# tell django to search ofr models changes, and store the changes as a migration.

python manage.py makemigrations <appname>  

# migrations are how django stores changes to your models (database schema | files on disk)

python manage.py migrate <appname>  # apply those changes to the database.

## The reason that they are separate commands to make and apply migrations is becuase you'll commit migrations to your version control system and ship them with you app;

### Views

# use class base View from Django 





```



##### Git commands


```
git checkout <old-branchname>       # switch to branchname
git checkout -b <new-branchname>    # create new branch 

```

##### Django Apps

* django.contrib.admin          – The admin site. You’ll use it shortly.
* django.contrib.auth           – An authentication system.
* django.contrib.contenttypes   – A framework for content types.
* django.contrib.sessions       – A session framework.
* django.contrib.messages       – A messaging framework.
* django.contrib.staticfiles    – A framework for managing static files.

```
# this command scans INSTALLED_APPS settings and creates any database tables accourding to the database settings from settings.py

python manage.py migrate


```


#### Django Testing

* Code without tests is broken by design"
    * write test before additional coding.
    * when a test fails, add more test to handle the raised exception.
    * proceed to refactor the code for the latest tests and additional unexpected tests.
    * until the code behave in expected ways.

* Test prevents having to solve the same problem twice over time. and also logs the bug history in a clean and handy fashion.

```
## test model

# create test cases
python -c "from django.test import TestCase; class <Appname><TestName>(TestCase):; def <testCaseName>"

# run tests
python manage.py test <appname> # have to implement tests.py with TestCase



## test view (script:testCase)

# create an instance of the client for our use.
python -c "from django.test import Client; client = Client()"

# have the client perform url requests to our domain and specify the expected response.
response = client.get('<url>')

# rather than hard code <url> use reverse()
response = client.get(reverse('<appname_ns>:<appview')

## test view (cli)

# setup cli environment
python -c "from django.test.utils import setup_test_environment; setup_test_environment()"

## live server testing (browser automation using selenium)... 

```



    
##### Packaging Reusable Apps

```
## Prerequisite

setuptools

pip

```

1. create app: <appname> | django-<appname> # helps others identify as django specific app
2. dev the app :construction_worker: :wrench: :nut_and_bolt:
3. [...](django-reusableapp/README.md)




##### Concepts

* Apps: is a Web application that does something.
* Project: a project is a collection of configuration and apps for a particular website.
* 1 Project can have N apps, 1 App can be in N projects.




##### Acronyms

* API : Application Program Interface
* ORM : Object Relational Mapping
