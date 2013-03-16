smokeping is an app for `Django <https://www.djangoproject.com/>` to configure your `Smokeping <http://oss.oetiker.ch/smokeping/>` installation

Dependencies
-----------

- django-mptt

Quick start
-----------

1. Add "smokeping" and "mptt" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'mptt',
          'smokeping',
      )

2. Add "middleware" to your MIDDLEWARE_CLASSES setting like this::

      MIDDLEWARE_CLASSES = (
          ...
          'smokeping.middleware.StripWhitespaceMiddleware',
      )

3. Include the polls URLconf in your project urls.py like this::

      url(r'^smokeping/', include('smokeping.urls')),

4. Run `python manage.py syncdb` to create the smokeping models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
  to start with smokeping (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/smokeping/ to view your configuration exported.

