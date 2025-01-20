from rest_framework import serializers

from apps.currency.models import CurrencyModel, CurrencyPointModel
from apps.currency.services import point_is_actual


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyModel

        fields = (
            'name',
        )


class CurrencyPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrencyPointModel

        fields = (
            'date_point', 'currency', 'saleRate', 'purchaseRate',
        )

