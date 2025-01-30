from rest_framework import serializers

from apps.city.models import CityModel


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel

        fields = (
            'region', 'name', 'value'
        )
