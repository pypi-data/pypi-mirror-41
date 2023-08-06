==================================================
:package: CRM [Package]
==================================================

Cloud Custom Connections

Production Environment.
-----------------------

Production URL:
    https://linkfusions.com
    
Storage Buckets:
    * Static files: gs://static.linkfusions.com/
    
    * Media files: gs://media.linkfusions.com/


Testing (dev) Environment, Standalone version:
---------------------------------------

Testing URL: 
    https://crm.cloudcustomsolutions.io

Storage Buckets:
    * Static files: gs://static.crm.cloudcustomsolutions.io/
    
    * Media files: gs://static.crm.cloudcustomsolutions.io

Quickstart
----------

Install ccc::

    pip install CCC

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'ccc.apps.CccConfig',
        ...
    )

Add ccc's URL patterns:

.. code-block:: python

    from ccc import urls as ccc_urls


    urlpatterns = [
        ...
        url(r'^', include(ccc_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox
