import django_filters # type: ignore

from api.models import Archer

class ArcherFilter(django_filters.FilterSet):
    class Meta:
        model = Archer
        fields = {
            'first_name': ['iexact', 'icontains'],
            'last_name': ['iexact', 'icontains'],
        }
