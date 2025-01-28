from rest_framework import serializers

from apps.car_model.models import CarModelModel


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModelModel

        fields = (
            'car_mark','name', 'value'
        )
        read_only_fields = ('car_mark',)