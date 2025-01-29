from rest_framework import serializers

from apps.currency.models import CurrencyModel, CurrencyPointModel


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyModel
        fields = ('name', 'saleRate', 'purchaseRate')
        read_only_fields = ('name', 'saleRate', 'purchaseRate')

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['name'] = self.context['name']
        attrs['saleRate'] = self.context['saleRate']
        attrs['purchaseRate'] = self.context['purchaseRate']
        return attrs

