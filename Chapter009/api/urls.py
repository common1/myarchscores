import uuid
from django.urls import path
from . import views

urlpatterns = [
    path('archers/', views.ArcherListAPIView.as_view(), name='archer-list'),
    path('archers/info/', views.ArcherInfoAPIView.as_view(), name='archer-info'),
    path('archers/<uuid:archer_id>/', views.ArcherDetailAPIView.as_view(), name='archer-detail'),
    path('clubs/', views.ClubListAPIView.as_view(), name='club-list'),
]