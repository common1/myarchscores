from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend  # type: ignore
from rest_framework import filters, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import (LimitOffsetPagination,
                                       PageNumberPagination)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.filters import ArcherFilter, ClubFilter
from api.models import Archer, Club
from api.serializers import (ArcherInfoSerializer, ArcherSerializer,
                             ClubSerializer)


class ArcherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Archer.objects.order_by('pk')
    serializer_class = ArcherSerializer
    filterset_class = ArcherFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    # Exact match: '=first_name', '=last_name'
    search_fields = ['first_name', 'last_name', 'info']
    ordering_fields = ['first_name', 'last_name']
    pagination_class = PageNumberPagination
    pagination_class.page_size = 2
    pagination_class.page_query_param = 'pagenum'
    pagination_class.page_size_query_param = 'size'
    pagination_class.max_page_size = 6

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

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.prefetch_related('memberships__archer').order_by('name')
    serializer_class = ClubSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None
    filterset_class = ClubFilter
    filter_backends = [
        DjangoFilterBackend,
    ]

class ArcherInfoAPIView(APIView):
    def get(self, request):
        archers = Archer.objects.all()
        serializer = ArcherInfoSerializer({
            'archers': archers,
            'count': len(archers),
        })
        return Response(serializer.data)

