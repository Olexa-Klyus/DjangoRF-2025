from rest_framework import serializers

from apps.adverts.models import AdvertModel
from apps.categories.serializers import CategorySerializer
from apps.currency.services import get_calculated_prices, get_currency_points, point_is_actual


class AdvertSearchSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_advert', read_only=True)

    class Meta:
        model = AdvertModel
        fields = ('title', 'mileage', 'region', 'city', 'price', 'currency', 'description', 'gearbox', 'fuel')
        read_only_fields = (
            'title', 'mileage', 'region', 'city', 'price', 'currency', 'description', 'gearbox', 'fuel')


class AdvertGetUserAutosSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_advert', read_only=True)

    class Meta:
        model = AdvertModel

        fields = ('id', 'user_id', 'title', 'categories', 'car_mark', 'car_model', 'year', 'mileage',
                  'region', 'city', 'profanity_edit_count', 'is_active',
                  'price', 'price_init', 'currency', 'description', 'gearbox', 'fuel', 'expired_at')

        depth = 1


class AdvertCreateUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title_advert', read_only=True)

    class Meta:
        model = AdvertModel

        fields = (
            'id', 'user_id', 'title', 'categories', 'car_mark', 'car_model', 'year', 'mileage',
            'region', 'city', 'profanity_edit_count',
            'price', 'price_init', 'currency', 'description', 'gearbox', 'fuel', 'expired_at'
        )
        read_only_fields = (
            'id', 'price_init', 'car_mark', 'car_model', 'user_id', 'expired_at', 'profanity_edit_count',)

        extra_kwargs = {'is_active': {'write_only': True, }}

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if 'price_init' in self.context:
            attrs['price_init'] = self.context['price_init']
        if 'car_mark' in self.context:
            attrs['car_mark'] = self.context['car_mark']
        if 'car_model' in self.context:
            attrs['car_model'] = self.context['car_model']
        return attrs


class AdvertGetInfoSerializer(serializers.ModelSerializer):
    categories = CategorySerializer()

    class Meta:
        model = AdvertModel

        fields = (
            'id', 'user_id', 'categories', 'car_mark', 'car_model', 'year', 'mileage', 'region', 'city', 'auto_salon',
            'price_init', 'price', 'currency', 'description', 'gearbox', 'fuel', 'created_at',
            'updated_at', 'expired_at'
        )

    def to_representation(self, instance):
        obj = super(AdvertGetInfoSerializer, self).to_representation(instance)

        if hasattr(instance, 'counter'):
            obj['counter'] = instance.counter
        if hasattr(instance, 'avg_prices'):
            obj['avg_prices'] = instance.avg_prices
        obj['calc_prices'] = get_calculated_prices(instance.price, instance.currency.id)
        obj['currency_points'] = get_currency_points()
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
