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

class ArcherListAPIView(generics.ListAPIView):
    queryset = Archer.objects.all()
    serializer_class = ArcherSerializer

class ArcherDetailAPIView(generics.RetrieveAPIView):
    queryset = Archer.objects.all()
    serializer_class = ArcherSerializer
    lookup_url_kwarg = 'archer_id'

class ClubListAPIView(generics.ListAPIView):
    queryset = Club.objects.prefetch_related('memberships__archer')
    serializer_class = ClubSerializer

# @api_view(['GET'])
# def club_list(request):
#     clubs = Club.objects.prefetch_related('memberships__archer')
#     serializer = ClubSerializer(clubs, many=True)

#     return Response(serializer.data)

@api_view(['GET'])
def archer_info(request):
    archers = Archer.objects.all()
    serializer = ArcherInfoSerializer({
        'archers': archers,
        'count': len(archers),
    })
    return Response(serializer.data)

