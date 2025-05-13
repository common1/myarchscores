from rest_framework import serializers
from .models import Archer, Club, Membership

class ArcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archer
        fields = (
            'id',
            'created_at',
            'modified_at',
            'last_name',
            'first_name',
            'middle_name',
            'slug',
            'union_number',
            'info',
            'author'
        )

class MembershipSerializer(serializers.ModelSerializer):
    # archer = ArcherSerializer(read_only=True)
    archer = serializers.StringRelatedField(
        read_only=True
    )

    class Meta:
        model = Membership
        fields = (
            'id',
            'created_at',
            'modified_at',
            'archer',
        )

class ClubSerializer(serializers.ModelSerializer):
    memberships = MembershipSerializer(many=True, read_only=True)

    class Meta:
        model = Club
        fields = (
            'id',
            'created_at',
            'modified_at',
            'name',
            'slug',
            'town',
            'info',
            'author',
            'memberships'
        )

