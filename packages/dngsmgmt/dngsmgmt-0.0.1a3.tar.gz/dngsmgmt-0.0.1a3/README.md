
dngsmgmt
-----------

dngsmgmt is a Django app to manage NGS projects 

Quick start
-----------

1. Add "dngsmgmt" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'dngsmgmt',
    ]

2. Include the dgenome URLconf in your project urls.py like this::

    url(r'^dngsmgmt/', include((dngsmgmt.urls, 'dngsmgmt'), namespace='dngsmgmt')),

3. Run `python manage.py makemigrations dngsmgmt` to create the dngsmgmt tables.

4. Run `python manage.py migrate` to create the dngsmgmt models.

