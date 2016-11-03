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


##### Django admin && manage.py [ref](https://docs.djangoproject.com/en/1.10/ref/django-admin/)

```

## Django-admin: idea of separation between content publishers and public site
# 

python manage.py createsuperuser

>prompted: <username>
>prompted: <email>
>prompted: <password>

## Django-admin section:
 
> http://<domain>:<port>/admin/






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

##### Django MVC

```

### Models

# tell django to search ofr models changes, and store the changes as a migration.

python manage.py makemigrations <appname>  

# migrations are how django stores changes to your models (database schema | files on disk)

python manage.py migrate <appname>  # apply those changes to the database.

## The reason that they are separate commands to make and apply migrations is becuase you'll commit migrations to your version control system and ship them with you app;



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




##### Concepts

* Apps: is a Web application that does something.
* Project: a project is a collection of configuration and apps for a particular website.
* 1 Project can have N apps, 1 App can be in N projects.




##### Acronyms

* API : Application Program Interface
* ORM : Object Relational Mapping