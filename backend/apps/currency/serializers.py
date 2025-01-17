from rest_framework import serializers

from apps.currency.models import CurrencyModel, CurrencyPointModel


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyModel

        fields = (
            'name',
        )


class CurrencyPointSerializer(serializers.ModelSerializer):
    # currency = CurrencySerializer()

    class Meta:
        model = CurrencyPointModel

        fields = (
            'date_point', 'currency', 'saleRate', 'purchaseRate', 'saleRateNB'
        )
