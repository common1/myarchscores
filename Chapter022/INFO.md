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

# Chapter012 - Part 1

Django REST Framework - JWT Authentication with djangorestframework-simplejwt
[https://www.youtube.com/watch?v=Xp0-Yy5ow5k&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=12]

TokenAuthentication
[https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication]

JSON Web Token Authentication
[https://www.django-rest-framework.org/api-guide/authentication/#json-web-token-authentication]

github jazzband/djangorestframework-simplejwt
[https://github.com/jazzband/djangorestframework-simplejwt]

Simple JWT
[https://django-rest-framework-simplejwt.readthedocs.io/en/latest/]

```
File: drf_course/settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

# Chapter012 - Part 2

```
$ pip install djangorestframework-simplejwt
$ pip freeze > requirements.txt

File: drf_course/settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

File: drf_course/urls.py
...
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

JSON Web Token (JWT) Debugger
[https://jwt.io/]

# Chapter012 - Part 3

...

## Chapter013 - Part 1

Django REST Framework - Refresh Tokens & JWT Authentication
[https://www.youtube.com/watch?v=H3OY36wa7Cs&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=13]

## Chapter014 - Part 1

Django REST Framework - Updating & Deleting data
[https://www.youtube.com/watch?v=08gHVFPFuBU&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=14]

## Chapter014 - Part 2

...

## Chapter015 - Part 1

drf-spectacular - Django REST Framework API Documentation
[https://www.youtube.com/watch?v=E3LUvsPWLwM&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=15]

tfranzel/drf-spectacular
[https://github.com/tfranzel/drf-spectacular]

## Chapter015 - Part 2

```
$ pip install drf-spectacular
$ pip freeze > requirements.txt

File: drf_course/settings.py
INSTALLED_APPS = [
    # ALL YOUR APPS
    'drf_spectacular',
]

REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Archery scores API',
    'DESCRIPTION': 'Archery scores API for managing archery scores and users',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

$ python manage.py spectacular --color --file schema.yml

File: archscore/urls.py
urlpatterns = [
    ...

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

```
Local
[http://localhost:8001/api]
[http://localhost:8001/api/schema/swagger-ui/]
[http://localhost:8001/api/schema/redoc/]

## Chapter016 - Part 1

django-filter and DRF API filtering - Django REST Framework
[https://www.youtube.com/watch?v=NDFgTGTI8zg&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=16]

[https://www.django-rest-framework.org/api-guide/filtering/]
[https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend]

```
$ pip install django-filter
$ pip freeze > requirements.txt 

File: archscore/settings.py
INSTALLED_APPS = [
    ...
    'django_filters',
    ...
]

REST_FRAMEWORK = {
    ...
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}
```

Local
[http://localhost:8001/archers/?first_name=Harrie]
[http://localhost:8001/archers/?first_name__icontains=arr]
[http://localhost:8001/archers/?last_name__icontains=uld]

## Chapter017 - Part 1

SearchFilter and OrderingFilter in Django REST Framework
[https://www.youtube.com/watch?v=LCYqDsl1WYI&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=17]

[https://www.django-rest-framework.org/api-guide/filtering/#searchfilter]
[https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter]

Local
[http://localhost:8001/archers/?search=smulde]
[http://localhost:8001/archers/?ordering=last_name]
[http://localhost:8001/archers/?ordering=-last_name]
[http://localhost:8001/archers/?ordering=first_name]
[http://localhost:8001/archers/?ordering=-first_name]

## Chapter018 - Part 1

Writing Filter Backends in Django REST Framework
[https://www.youtube.com/watch?v=u4S71cO5QhI&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=18]

[https://www.django-rest-framework.org/api-guide/filtering/#custom-generic-filtering]

...

## Chapter019 - Part 1

API Pagination - Django REST Framework | PageNumberPagination & LimitOffsetPagination
[https://www.youtube.com/watch?v=sTyMe2R9mzk&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=19]

[https://www.django-rest-framework.org/api-guide/pagination/]
[https://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination]

```
REST_FRAMEWORK = {
    ...
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
}
```

Local
[http://localhost:8001/archers/]
[http://localhost:8001/archers/?page=2]

[http://localhost:8001/archers/?ordering=last_name]
[http://localhost:8001/archers/?ordering=last_name&page=2]

[http://localhost:8001/archers/?size=3]

## Chapter020 - Part 1

Viewsets & Routers in Django REST Framework
[https://www.youtube.com/watch?v=4MrB4IvW6Ow&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=20]

[https://www.django-rest-framework.org/api-guide/viewsets/]
[https://www.cdrf.co/]
[https://www.cdrf.co/3.14/rest_framework.viewsets/ModelViewSet.html]
[https://www.django-rest-framework.org/api-guide/routers/]

## Chapter020 - Part 2

...

## Chapter021 - Part 1

Viewset Actions, Filtering and Permissions in Django REST Framework
[https://www.youtube.com/watch?v=rekvVrjUMjg&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=21]

```
$ pip install isort
$ pip freeze > requirements.txt
$ isort ./api/views.py
```

Local
[http://localhost:8001/clubs/?create_at__gt=2025-05-15]
[http://localhost:8001/clubs/?created_at__lt=2025-05-15]
[http://localhost:8001/clubs/?created_at=2025-05-15]

## Chapter022 - Part 1

Viewset Permissions | Admin vs. Normal User in Django
[https://www.youtube.com/watch?v=KmYYg1qJKNQ&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=22]

