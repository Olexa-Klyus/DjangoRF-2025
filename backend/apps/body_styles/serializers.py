from rest_framework import serializers

from apps.body_styles.models import BodyStylesModel


class BodyStylesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyStylesModel

        fields = (
            'name', 'value', 'parent_id', 'category_id'
        )
