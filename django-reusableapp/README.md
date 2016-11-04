

[Reusable Apps](https://docs.djangoproject.com/en/1.10/intro/reusable-apps/)


```
# generate the dist directory and builds a new django package.

python setup.py sdist # run from inside django-<appname>



# install

pip install --user django-<appname>/dist/django-<appname>-x.x.tar.gz

# uninstall

pip uninstall django-<appname>

# publish the package on a public repo. [https://pypi.python.org/pypi]
# how to publish https://packaging.python.org/

```