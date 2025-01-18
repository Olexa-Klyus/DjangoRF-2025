from json import JSONEncoder

from rest_framework import serializers

from apps.adverts.models import AdvertModel
from apps.categories.serializers import CategorySerializer
from apps.currency.models import CurrencyPointModel


class AdvertCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertModel

        fields = (
            'title', 'user_id', 'categories', 'brand', 'mark', 'year', 'mileage',
            'region', 'city',
            'price', 'currency', 'description', 'gearbox', 'fuel', 'expired_at'
        )


class AdvertPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertModel
        fields = ('photo',)


class AdvertAutoSalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertModel
        fields = ('auto_salon',)


class AdvertGetInfoSerializer(serializers.ModelSerializer):
    categories = CategorySerializer()

    class Meta:
        model = AdvertModel

        fields = (
            'id', 'user_id', 'categories', 'brand', 'mark', 'year', 'mileage', 'region', 'city', 'auto_salon',
            'price_init', 'price', 'currency', 'description', 'gearbox', 'fuel', 'created_at', 'updated_at',
            'expired_at'
        )
        # depth = 1

    def to_representation(self, instance):
        obj = super(AdvertGetInfoSerializer, self).to_representation(instance)
        query_set = CurrencyPointModel.objects.values()[:2]
        points = []

        for item in query_set:
            points.append({
                "currency_point_date": item["date_point"],
                "currency_id": item["currency_id"],
                'saleRate': item['saleRate'],
                'purchaseRate': item['purchaseRate'],
            })

        # date_point = last_points[0]['date_point']

        # print(date_point)
        # points = {"currency_point_date": date_point}

        obj['currency_points'] = points
        print('inside to representation', obj)
        return obj
