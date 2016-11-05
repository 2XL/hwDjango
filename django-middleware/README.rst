

=======
AppName
=======


<description>




Quick start
-----------


1.  Add "<appname>" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        '<appname>',
    ]

2. Include the <appname> URLconf in your project urls.py like this::

    url(r'^<appname>/', include('<appname>.urls')),

3. Run `python manage.py migrate` to create the <appname> models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a <appname> (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/<appname>/ to participate in the <appname>.