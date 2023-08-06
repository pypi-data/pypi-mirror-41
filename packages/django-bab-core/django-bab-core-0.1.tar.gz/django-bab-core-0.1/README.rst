=====
bab CMS
=====

Light CMS Django app.

Quick start
-----------

1. Add "bab_cms" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'bab_cms',
    ]

2. Include the cms URLconf in your project urls.py like this::

    path('cms/', include('bab_cms.urls')),

3. Run `python manage.py migrate` to create the cms models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create posts and articles (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/cms/ to participate in the CMS.
