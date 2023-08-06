=====
bab CMS
=====

Light CMS Django app.

Quick start
-----------

1. Add "bab_cms" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'bab_core',
    ]

2. Include the cms URLconf in your project urls.py like this::

    path('core/', include('bab_core.urls')),

3. Run `python manage.py migrate` to create the cms models.
