*django-smokeping* is an app for [Django](https://www.djangoproject.com/) to configure your [Smokeping](http://oss.oetiker.ch/smokeping/) installation.

# Dependencies
* django-mptt

# Installation
Install the extension with `pip` :
```shell
$ pip install git+git://github.com/julcollas/django-smokeping.git
```
or alternatively if you don't have pip installed :

```shell
$ python setup.py install
```
# Quick start

1.  Add "smokeping" and "mptt" to your INSTALLED\_APPS setting like this:
    ```
    INSTALLED_APPS = ( ... 'mptt', 'smokeping', )
    ```
2.  Add "middleware" to your MIDDLEWARE\_CLASSES setting like this:
    ```
    MIDDLEWARE\_CLASSES = ( ...
      'smokeping.middleware.StripWhitespaceMiddleware',
    )
    ```
3.  Include the polls URLconf in your project urls.py like this:
    ```
    url(r'\^smokeping/', include('smokeping.urls')),
    ```
4.  Run `python manage.py syncdb` to create the smokeping models.
5.  Start the development server and visit http://127.0.0.1:8000/admin/ to start with smokeping (you'll need the Admin app enabled).
6.  Visit http://127.0.0.1:8000/smokeping/ to view your configuration exported.

# Docker && Compose
## Build image
```shell
$ docker build . -t smokepingadmin
```
## docker-compose example
```yaml
version: "3"
services:
  smokepingadmin:
    container_name: smokepingadmin
    image: smokepingadmin
    volumes:
      - ./smokepingadmin/db/:/app/demo/db
    depends_on:
      - smokepingadmin_sync

  smokepingadmin_sync:
    image: smokepingadmin
    command: bash -c "python manage.py syncdb --noinput"
    volumes:
      - ./smokepingadmin/db/:/app/demo/db
```

# Usage

1.  You will find a config file example in "tools". Put it in your smokeping directory "/etc/smokeping/"
2.  You will find a get\_config.py script example in "tools". Put it in your smokeping directory "/etc/smokeping/config.d/"
3.  You will find a smokeping-get-config.cron example in "tools". Put it in your cron directory "/etc/cron.d/"
