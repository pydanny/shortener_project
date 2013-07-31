========================
Shortener Project
========================

A Django project for creating and maintaining shortUrls.


Run the Tests
================

::

    coverage run manage.py test --settings=shortener.settings.test
    
Deploy the site
================

::

    $ make createsite
    $ heroku config:add SECRET_KEY=<CHANGE_ME>