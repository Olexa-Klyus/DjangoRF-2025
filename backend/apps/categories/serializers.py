from rest_framework import serializers

from apps.categories.models import CategoryModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('name', 'value',)

    # def to_representation(self, instance):
    #     obj = super(CategorySerializer, self).to_representation(instance)
    #
    #     obj['label'] = obj['name']
    #     return obj
