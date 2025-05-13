import uuid
from django.urls import path
from . import views

urlpatterns = [
    path('archers/', views.archer_list, name='archer-list'),
    path('archers/info/', views.archer_info, name='archer-info'),
    path('archers/<uuid:pk>/', views.archer_detail, name='archer-detail'),
    path('clubs/', views.club_list, name='club-list'),
]