import uuid
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('archers/', views.ArcherListCreateAPIView.as_view(), name='archer-list'),
    path('archers/info/', views.ArcherInfoAPIView.as_view(), name='archer-info'),
    path('archers/<uuid:archer_id>/', views.ArcherDetailAPIView.as_view(), name='archer-detail'),
    path('users/', views.UserListView.as_view(), name='user_list'),
]

router = DefaultRouter()
router.register(r'clubs', views.ClubViewSet, basename='club')
urlpatterns += router.urls

