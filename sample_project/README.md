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

    OR

    > python manage.py runserver --settings=sample_project.setting.development
```

## To apply db changes
```
    python manage.py makemigrations
    python manage.py migrate
```

## When 404.html will work?
```
    DEBUG = False
    ALLOWED_HOSTS = ['www.x-y-z.com']
```







Django Doc: https://docs.djangoproject.com/en/4.1/intro/
