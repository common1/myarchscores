from django.db import transaction
from rest_framework import serializers
from .models import Archer, Club, Membership, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'is_staff',
        )

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
            'union_number',
            'info',
            'author'
        )

class MembershipSerializer(serializers.ModelSerializer):
    # archer = ArcherSerializer(read_only=True)
    # archer = serializers.StringRelatedField(
    #     read_only=True
    # )
    archer = serializers.StringRelatedField()

    class Meta:
        model = Membership
        fields = (
            'id',
            'created_at',
            'modified_at',
            'archer',
        )

class ClubCreateSerializer(serializers.ModelSerializer):
    class MembershipSerializer(serializers.ModelSerializer):
        class Meta:
            model = Membership
            fields = (
                'archer',
            )

    id = serializers.UUIDField(read_only=True)
    memberships = MembershipSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        membership_data = validated_data.pop('memberships')

        with transaction.atomic():
            instance = super().update(instance, validated_data)

            if membership_data is not None:
                instance.memberships.all().delete()
                for membership in membership_data:
                    Membership.objects.create(club=instance, **membership)

        return instance

    def create(self, validated_data):
        membership_data = validated_data.pop('memberships')

        with transaction.atomic():
            club = Club.objects.create(**validated_data)
            for membership in membership_data:
                Membership.objects.create(club=club, **membership)

        return club

    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'slug',
            'town',
            'info',
            'author',
            'memberships',
        )

class ClubSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
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

class ArcherInfoSerializer(serializers.Serializer):
    archers = ArcherSerializer(many=True, read_only=True)
    count = serializers.IntegerField(read_only=True)
