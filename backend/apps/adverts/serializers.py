from rest_framework import serializers

from apps.adverts.models import AdvertModel
from apps.categories.serializers import CategorySerializer
from apps.currency.services import get_calculated_prices, get_last_points, point_is_actual


class AdvertCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertModel

        fields = (
            'title', 'user_id', 'categories', 'brand', 'mark', 'year', 'mileage',
            'region', 'city',
            'price', 'price_init', 'currency', 'description', 'gearbox', 'fuel', 'expired_at'
        )


class AdvertGetInfoSerializer(serializers.ModelSerializer):
    categories = CategorySerializer()

    class Meta:
        model = AdvertModel

        fields = (
            'id', 'user_id', 'categories', 'brand', 'mark', 'year', 'mileage', 'region', 'city', 'auto_salon',
            'price_init', 'price', 'currency', 'description', 'gearbox', 'fuel', 'created_at', 'updated_at',
            'expired_at'
        )

    def to_representation(self, instance):
        obj = super(AdvertGetInfoSerializer, self).to_representation(instance)

        # if hasattr(instance, 'counter'):
        #     obj['counter'] = instance.counter
        if hasattr(instance, 'count_all'):
            obj['count_all'] = instance.count_all
        obj['calc_prices'] = get_calculated_prices(instance.price, instance.currency)
        obj['currency_points'] = get_last_points()
        obj['point_is_actual'] = point_is_actual()

        return obj


class AdvertPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertModel
        fields = ('photo',)


class AdvertAutoSalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertModel
        fields = ('auto_salon',)
