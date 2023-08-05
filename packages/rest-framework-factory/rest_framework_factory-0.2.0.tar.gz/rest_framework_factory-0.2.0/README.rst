=============================
Rest Framework Factory (DRFF)
=============================


.. image:: https://img.shields.io/pypi/v/rest_framework_factory.svg
        :target: https://pypi.python.org/pypi/rest_framework_factory

.. image:: https://img.shields.io/travis/MiddleFork/rest_framework_factory.svg
        :target: https://travis-ci.org/MiddleFork/rest_framework_factory

.. image:: https://readthedocs.org/projects/rest-framework-factory/badge/?version=latest
        :target: https://rest-framework-factory.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/MiddleFork/rest_framework_factory/shield.svg
     :target: https://pyup.io/repos/github/MiddleFork/rest_framework_factory/
     :alt: Updates



A factory for creating Django Rest Framework APIs



* Documentation: https://rest-framework-factory.readthedocs.io.


Features
--------

* Create a DRF API painlessly, without needing to repeat boilerplate code

Installation
------------

*    ``pip install rest_framework_factory``

Requirements
------------

* A Django project with at least one app' from which you wish to build an DRF API included in INSTALLED_APPS, and with at least one model defined in models.py


How it Works
------------

* The Factory works because a model itself contains all the information required in order to generate an API for it, including a Serializer, a Viewset, URL(s) and other optional (e.g. Forms, Filters) content

* Template files contain variable placeholders referencing the name and attributes of a model

TODOs
-----

* WEB UI interface to generate factory apis interactively

* Configuration files (YML?) to allow fine-grained control of the factory API, e.g. by including/excluding individual models and/or fields, setting allowed methods, etc.

* Swagger

* Sphinx

Usage
-----

Basic Usage - Manual Creation
+++++++++++++++++++++++++++++

* It is not necessary to add rest_framework_factory to INSTALLED_APPS

* One common use case is to build a factory using all the models defined in an app::

    from rest_framework_factory import factory
    drff = factory.Factory()
    drff.build_from_app('my_app')
    content = drff.apis['app']['my_app']
    with open('/tmp/drff_api.py')), 'w') as f:
        f.write(data)

* Once the factory file is built, it should be placed into the apps' folder, added to INSTALLED_APPS, and have its urls wired into the project::

    mkdir my_app/drff; touch my_app/drff/__init__.py; cp /tmp/drff_api.py ./my_app/drff/api.py


  * settings.py::

      INSTALLED_APPS += 'my_app.drff'

  * urls.py::

      from my_app.drff.api import urlpatterns as drff_urls
      urlpatterns += drff_urls



Using the Factory UI
++++++++++++++++++++

* TODO

  * Scan all the apps, the models therein, and their fields

  * Build forms for each model/app

  * Toggle desired models/fields on-off

  * Select serializer type (ie ModelSerializer vs ReadOnlyModelSerializer

  * Select allowed API endpoint methos (ie GET, POST)

Configuring the factory via YML
+++++++++++++++++++++++++++++++

* TODO

  *  Initiallize:  Scan all apps, the models therein, and their fields; write structure to file
    *  Manually edit file, comment out undesired fields and models, change permissions, etc

  *  Implement: Read yml file, generate factory

Credits
-------

Django_



Package created with Cookiecutter_.

.. _Django: https://github.com/django/django
.. _Cookiecutter: https://github.com/audreyr/cookiecutter

