from rest_framework import serializers

from apps.car_mark.models import CarMarkModel
from apps.car_model.models import CarModelModel
from apps.city.models import CityModel
from apps.region.models import RegionModel


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel

        fields = (
            'name', 'value'
        )
