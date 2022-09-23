# Read Guide


## To specify the settings manually
- when multiple settings files
```
    python manage.py runserver --settings=sample_project.settings_dev
```
- when settings folder
```
    > export DJANGO_SETTINGS_MODULE=sample_project.setting.development
    > python manage.py runserver
    > python manage.py runserver 9090
    > python manage.py runserver localhost:8000
    > python manage.py runserver 1.2.3.4:7000
    > python manage.py runserver [2001:0db8:1234:5678::9]:7000

    OR

    > python manage.py runserver --settings=sample_project.setting.development
```

## To apply & reflect db changes
```
    python manage.py makemigrations
    python manage.py migrate

    > python manage.py makemigrations app_name [for specific app]
    > python manage.py migrate app_name migrations_files_name

    > python manage.py migrate --skip-checks [skip migration]
```

## To connect with shell directly
```
    python manage.py shell
```

## To connect with dbshell directly
```
    python manage.py dbshell
```

## When 404.html will work?
```
    DEBUG = False
    ALLOWED_HOSTS = ['www.x-y-z.com']
```

## To collect all static files used in projects [will collect on STATIC_ROOT='' path]
```
    python manage.py collectstatic --clear
```

## dump data
```
    python manage.py dumpdata -o sampledata.json

    python manage.py dumpdata --exclude=auth --exclude=contenttypes -o sampledata.json
```

## load data
```
    python manage.py loaddata sampledata.json
```

## create superuser
```
    python manage.py createsuperuser
```

## change password
```
    python manage.py changepassword <user-name>
```

## clear session data
```
    python manage.py clearsessions
```

## django cache setup
1. Redis -> Redis is an in-memory database 
2. Memcached-> Memcached keeps its data in memory

- Should I use Memcache or Redis? 
>Redis uses a single core and shows better performance than Memcached in storing small datasets when measured in terms of cores. Memcached implements a multi-threaded architecture by utilizing multiple cores. Data is stored in memory (or RAM). If a server crashes, all the data stored is lost. Therefore, for storing larger datasets, Memcached can perform better than Redis.

- pymemcache [Memcached]
```
    https://pymemcache.readthedocs.io/en/latest/getting_started.html
```

- cache setup with Database caching
```
    python manage.py createcachetable
```

- Dummy caching (for development)
```
    CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
```

- The per-site cache
```
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]
```

- The per-view cache
```
    from django.views.decorators.cache import cache_page

    @cache_page(60 * 15)
    def your_view(request):
        pass

    # or

    urlpatterns = [
        path('object/<int:object_id>/', cache_page(60 * 15)(your_view)),
    ]
```

- Low-level cache API
```
    from django.core.cache import cache
    # cache.set(key, value, timeout=DEFAULT_TIMEOUT, version=None)
    # cache.get(key, default=None, version=None)

    cache.set('my_key', 'hello, world!', 30) # 30 second
    cache.get('my_key')
    cache.delete('objects')

    cache.add('add_key', 'New value', 30)
    cache.get_or_set('my_key', 'my new value', 100)
    cache.set_many({'a': 1, 'b': 2, 'c': 3})
    cache.delete_many(['a', 'b', 'c'])
    
    cache.clear()

    # cache versioning
    cache.set('my_key', 'hello world!', version=2)
    cache.get('my_key', version=2)
```


# Django Reference
https://books.agiliq.com/en/latest/README.html








# Django Doc
https://docs.djangoproject.com/en/4.1/topics/
