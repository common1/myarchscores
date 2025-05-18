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

# Chapter002 - Part 1

Django REST Framework - Serializers & Response objects | Browsable API
[https://www.youtube.com/watch?v=BMym71Dwox0&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=2]

Installation
[https://www.django-rest-framework.org/#installation]

Serializers
[https://www.django-rest-framework.org/api-guide/serializers/]

Serializers#Validation
[https://www.django-rest-framework.org/api-guide/serializers/#validation]

Serializer fields
[https://www.django-rest-framework.org/api-guide/fields/]

The Browsable API
[https://www.django-rest-framework.org/topics/browsable-api/]

Local
[http://localhost:8000/archers/?format=json]
[http://localhost:8000/archers/?format=api]
[http://localhost:8001/archers/0556f47f-2c65-4af7-ad8c-285aeb465adf/]

```
File: archscore/settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
]

```

# Chapter003 - Part 1

Django REST Framework- Nested Serializers, SerializerMethodField and Serializer Relations
[https://www.youtube.com/watch?v=KfSYadIFHgY&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=3]

Serializer relations
[https://www.django-rest-framework.org/api-guide/relations/]

# Chapter004 - Part 1

Django REST Framework - Serializer subclasses and Aggregated API data
[https://www.youtube.com/watch?v=_xbI0-mjtw4&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=4]

# Chapter005 - Part 1

django-silk for Profiling and Optimization with Django REST Framework
[https://www.youtube.com/watch?v=OG8alXR4bEs&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=5]

```
$ pip install django-silk
$ pip freeze > requirements.txt

File: drf_course/settings.py
MIDDLEWARE = [
    ...
    'silk.middleware.SilkyMiddleware',
    ...
]

INSTALLED_APPS = (
    ...
    'silk',
)

File: drf_course/urls.py
urlpatterns = [
    ...
    path('silk/', include('silk.urls', namespace='silk'))
]

$ python manage.py migrate
```

# Chapter006 - Part 1

Django REST Framework - Generic Views | ListAPIView & RetrieveAPIView
[https://www.youtube.com/watch?v=vExjSChWPWg&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=6]

Generic Views
[https://www.django-rest-framework.org/api-guide/generic-views/]

# Chapter006 - Part 2

...

# Chapter007 - Part 1

Django REST Framework - Dynamic Filtering | Overriding get_queryset() method
[https://www.youtube.com/watch?v=3Gi-w4Swge8&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=7]

```
$ python mange.py createsuperuser
User: ubuntuuser
Password: u***r
```

# Chapter007 - Part 2

...

# Chapter008 - Part 1

Django REST Framework - Permissions and Testing Permissions
[https://www.youtube.com/watch?v=rx5IV_4Iuog&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=8]

# Chapter009 - Part 1

Django REST Framework - APIView class
[https://www.youtube.com/watch?v=TVFCU0w65Ak&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=9]

# Chapter010 - Part 1

Django REST Framework - Creating Data | ListCreateAPIView and Generic View Internals
[https://www.youtube.com/watch?v=Jh85U1nhMh8&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=10]

# Chapter010 - Part 2

Classy Django REST Framework
[https://www.cdrf.co/]

# Chapter011 - Part 1

Django REST Framework - Customising permissions in Generic Views | VSCode REST Client extension
[https://www.youtube.com/watch?v=mlQZ1i8rUKQ&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=11]

Install REST Client Extension

