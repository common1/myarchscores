from rest_framework import serializers
from .models import Archer, Club, Membership

class ArcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archer
        fields = (
            'id',
            'last_name',
            'first_name',
            'middle_name',
            'slug',
            'union_number',
            'info',
            'author'
        )
    