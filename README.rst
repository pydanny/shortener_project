========================
Shortener Project
========================

A Django project for creating and maintaining shortUrls.

Plan
=====================

1. Create the shortener project.
2. Document every line of code.
3. Document every step taken.
4. Turn into a tutorial.


Steps Taken Thus Far
====================

.. note:: This will get moved into the docs folder.

Initial Creation::

    $ django-admin.py startproject --template=https://github.com/twoscoops/django-twoscoops-project/zipball/master --extension=py,rst,html shortener
    $ mv shortener shortener_project
    $ cd shortener_project

Command-Line Git work::

    $ git init
    $ git add .
    $ git commit -m "initial commit"
    $ git remote add origin git@github.com:pydanny/shortener_project.git

Added to Read the Docs:

    1. Logged in
    2. Created shortener_project

Created links app::

    $ cd shortener
    $ django-admin.py startapp links


Command Actions
================

::

    coverage run manage.py test --settings=shortener.settings.test