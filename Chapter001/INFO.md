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
django-admin startapp api
# File: archscore/settings.py
INSTALLED_APPS = [
    ...
    'api',
]
```

