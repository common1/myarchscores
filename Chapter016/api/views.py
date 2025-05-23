from django.shortcuts import get_object_or_404
from api.serializers import (
    ArcherSerializer,
    ClubSerializer,
    ArcherInfoSerializer,
)
from api.models import (
    Archer,
    Club
)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny,
)
from rest_framework.views import APIView
from api.filters import ArcherFilter

class ArcherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Archer.objects.all()
    serializer_class = ArcherSerializer
    filterset_class = ArcherFilter

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class ArcherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Archer.objects.all()
    serializer_class = ArcherSerializer
    lookup_url_kwarg = 'archer_id'

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class ClubListAPIView(generics.ListAPIView):
    queryset = Club.objects.prefetch_related('memberships__archer')
    serializer_class = ClubSerializer
    permission_classes = [IsAuthenticated]

class ArcherInfoAPIView(APIView):
    def get(self, request):
        archers = Archer.objects.all()
        serializer = ArcherInfoSerializer({
            'archers': archers,
            'count': len(archers),
        })
        return Response(serializer.data)

