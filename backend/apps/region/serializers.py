from rest_framework import serializers

from apps.region.models import RegionModel


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionModel
        fields = ('name', 'value')
