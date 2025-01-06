from rest_framework import serializers

from apps.auto_salon.models import AutoSalonModel


class AutoSalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoSalonModel
        fields = ('id', 'name',)
