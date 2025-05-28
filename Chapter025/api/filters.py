import django_filters # type: ignore

from api.models import Archer, Club

class ArcherFilter(django_filters.FilterSet):
    class Meta:
        model = Archer
        fields = {
            'last_name': ['iexact', 'icontains'],
        }

class ClubFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(field_name='created_at__date')
    class Meta:
        model = Club
        fields = {
            'name': ['iexact', 'icontains'],
            'created_at': ['lt', 'gt', 'exact'],
        }