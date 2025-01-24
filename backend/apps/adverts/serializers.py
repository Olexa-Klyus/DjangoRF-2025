from rest_framework import serializers

from better_profanity import profanity

from apps.adverts.models import AdvertModel
from apps.categories.serializers import CategorySerializer
from apps.currency.services import get_calculated_prices, get_currency_points, point_is_actual


class AdvertCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertModel

        fields = (
            'id', 'title', 'user_id', 'categories', 'brand', 'mark', 'year', 'mileage',
            'region', 'city',
            'price', 'price_init', 'currency', 'description', 'gearbox', 'fuel', 'expired_at'
        )

        # from better_profanity import profanity
        #
        # class ProfanityChecker:
        #
        #     def check_profanity(self, data: dict):
        #         print(data)
        #         if data["profanity_edit_count"] > 4:
        #             return "Deactivate"
        #         if profanity.contains_profanity(data["title"]):  # True or False
        #             data["profanity_edit_count"] += 1
        #             return False
        #         if profanity.contains_profanity(data["description"]):  # True or False
        #             data["profanity_edit_count"] += 1
        #             return False
        #         return data

 # def validate_price(self, price):
 #        if price <= 0:
 #            raise serializers.ValidationError('Price must be greater than 0')
 #        return price
 #
 #    def validate(self, attrs):
 #        price = attrs.get('price')
 #        size = attrs.get('size')
 #
 #        if price == size:
 #            raise serializers.ValidationError('Price cannot be equal to size')


class AdvertGetInfoSerializer(serializers.ModelSerializer):
    categories = CategorySerializer()

    # currencies = CurrencySerializer()

    class Meta:
        model = AdvertModel

        fields = (
            'id', 'user_id', 'categories', 'brand', 'mark', 'year', 'mileage', 'region', 'city', 'auto_salon',
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
