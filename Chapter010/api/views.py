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
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ArcherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Archer.objects.all()
    serializer_class = ArcherSerializer
    # permission_classes = [IsAuthenticated]

class ArcherDetailAPIView(generics.RetrieveAPIView):
    queryset = Archer.objects.all()
    serializer_class = ArcherSerializer
    lookup_url_kwarg = 'archer_id'
    # permission_classes = [IsAuthenticated]

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

