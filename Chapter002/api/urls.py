import uuid
from django.urls import path
from . import views

urlpatterns = [
    path('archers/', views.archer_list, name='archer-list'),
    path('archers/<uuid:pk>/', views.archer_detail, name='archer-detail'),
]