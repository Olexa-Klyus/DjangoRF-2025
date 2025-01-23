from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.currency.models import CurrencyModel
from apps.currency.serializers import CurrencyPointSerializer, CurrencySerializer


class CurrencyPointUpdateView(GenericAPIView):
    queryset = CurrencyModel.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['patch']
    lookup_field = 'name'

    def patch(self, *args, **kwargs):
        currency_obj = self.get_object()
        data = self.request.data

        data['saleRate'] = data['buy']
        data['purchaseRate'] = data['sale']

        serializer = CurrencySerializer(currency_obj, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data['currency'] = currency_obj.id
        self._add_currency_poit_to_arj()

        return Response(serializer.data, status.HTTP_200_OK)

    def _add_currency_poit_to_arj(self):
        data = self.request.data

        serializer = CurrencyPointSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return 'point is add'
