from rest_framework import serializers

from apps.adverts.models import AdvertModel


class AdvertCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertModel

        fields = (
            'id', 'title', 'user_id', 'categories', 'brand', 'car_model', 'year', 'mileage', 'boby_style',
            'region', 'city',
            'price', 'currency', 'description', 'gearbox', 'fuel', 'created_at', 'updated_at', 'expired_at'
        )


class AdvertGetInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertModel

        fields = (
            'id', 'user_id', 'categories', 'brand', 'car_model', 'year', 'mileage', 'boby_style',
            'region', 'city',
            'price', 'currency', 'description', 'gearbox', 'fuel', 'created_at', 'updated_at', 'expired_at'
        )
        depth = 1
