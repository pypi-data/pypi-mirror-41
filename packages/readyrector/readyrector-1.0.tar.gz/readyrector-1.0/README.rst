***********
ReadyRector
***********

.. image:: https://badge.fury.io/py/readyrector.png
    :target: https://badge.fury.io/py/readyrector

Easy to implement redirect middleware, which loads redirects from a configurable backend.

Installation
============

.. code-block:: sh

    pip install readyrector


Usage
=====

.. code-block:: python

        # settings.py
        INSTALLED_APPS = (
            # ...
            'readyrector',
            # ...
        )

        # put at the end of the middleware list as a last resort
        MIDDLEWARE = (
            # ...
            'readyrector.middleware.RedirectDatabaseMiddleware',
        )


RedirectDatabaseMiddleware
--------------------------

Gets redirects from database records. Implement a view or API to manage these records.

RedirectURLConfMiddleware
-------------------------

Gets redirects from a URL conf file. Requires setting ``READYRECTOR_URLCONF``


Settings
========

``READYRECTOR_URLCONF``
-----------------------

- Default: ``''``

Required when ``RedirectURLConfMiddleware`` is used. Expects a path to a URL conf file.
