from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.user.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = (
            'id', 'name', 'surname', 'created_at', 'updated_at'
        )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at', 'profile'
        )
        read_only_fields = (
            'id', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        profile = ProfileModel.objects.create(**profile, user=user)
        return user
