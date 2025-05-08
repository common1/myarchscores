# archscore

Django REST Framework Series
[https://www.youtube.com/playlist?list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t]

# Chapter001 - Part 1

Django REST Framework series - Setup and Models
[https://www.youtube.com/watch?v=6AEvlNgRPNc&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=1]

```
# Create virtual environment and install packages
$ python3 -m venv venv-drf
$ source venv-drf/bin/activate
$ pip install -r requirements.txt
```

```
# Create application
$ django-admin startproject archscore .

# Create api
$ django-admin startapp api

# File: archscore/settings.py
INSTALLED_APPS = [
    ...
    'api',
]
```

# Chapter001 - Part 2

See also: [https://pypi.org/project/django-faker/]

```
$ pip install django-faker
File: archscore/settings.py
INSTALLED_APPS = [
    ...
    'django_faker',
]

Create models:
# File: api/models.py
User
Basemodel
Archer
Club
Membership


$ python manage.py makemigrations
$ python manage.py migrate
```

# Chapter001 - Part 3

```
$ python manage.py populate_db

$ python manage.py graph_models api > models.dot
```

