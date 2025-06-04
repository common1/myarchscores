from django.db import transaction
from rest_framework import serializers
from .models import Archer, Club, Membership, User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    This serializer includes fields for username, email, is_staff, and is_superuser.
    It is used to represent user information in the API.
    """
    class Meta:
        """
        Meta class for UserSerializer.
        It specifies the model to be serialized and the fields to include.
        """

        # Model to be serialized
        model = User

        # Fields to include in the serialized output
        fields = (
            'username',
            'email',
            'is_staff',
            'is_superuser',
        )

class ArcherSerializer(serializers.ModelSerializer):
    """
    Serializer for the Archer model.
    This serializer includes fields for the archer's personal information,
    such as last name, first name, middle name, union number, and additional info.
    It also includes a reference to the author (User) of the archer record.
    """

    class Meta:
        """
        Meta class for ArcherSerializer.
        It specifies the model to be serialized and the fields to include.
        """

        # Model to be serialized
        model = Archer

        # Fields to include in the serialized output
        fields = (
            'id',
            'created_at',
            'modified_at',
            'last_name',
            'first_name',
            'middle_name',
            'union_number',
            'info',
            'author',
        )

class MembershipSerializer(serializers.ModelSerializer):
    """
    Serializer for the Membership model.
    This serializer includes a reference to the archer associated with the membership.
    It is used to represent membership information in the API.
    """
    
    # archer field is represented as a string (using StringRelatedField)
    archer = serializers.StringRelatedField()

    class Meta:
        """
        Meta class for MembershipSerializer.
        It specifies the model to be serialized and the fields to include.
        """

        # Model to be serialized
        model = Membership

        # Fields to include in the serialized output
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
