from unicodedata import category

from rest_framework import serializers

from apps.car_mark.models import CarMarkModel


class CarMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMarkModel

        fields = (
            'category', 'name', 'value'
        )
