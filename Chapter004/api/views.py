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

@api_view(['GET'])
def archer_list(request):
    archers = Archer.objects.all()
    serializer = ArcherSerializer(archers, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def archer_detail(request, pk):
    archer = get_object_or_404(Archer, pk=pk)
    serializer = ArcherSerializer(archer)

    return Response(serializer.data)

@api_view(['GET'])
def club_list(request):
    clubs = Club.objects.all()
    serializer = ClubSerializer(clubs, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def archer_info(request):
    archers = Archer.objects.all()
    serializer = ArcherInfoSerializer({
        'archers': archers,
        'count': len(archers),
    })
    return Response(serializer.data)

