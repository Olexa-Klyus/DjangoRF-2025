from rest_framework import serializers

from apps.car_model.models import CarModelModel


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModelModel

        fields = (
            'name', 'value'
        )
