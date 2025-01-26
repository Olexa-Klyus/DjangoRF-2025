from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.currency.models import CurrencyModel
from apps.currency.serializers import CurrencyPointSerializer, CurrencySerializer


class CurrencyPointCreateView(GenericAPIView):
    queryset = CurrencyModel.objects.all()
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data

        data['name'] = data['ccy']
        data['saleRate'] = data['buy']
        data['purchaseRate'] = data['sale']

        serializer = CurrencySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CurrencyPointUpdateView(GenericAPIView):
    queryset = CurrencyModel.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['patch', ]
    lookup_field = 'name'

    def patch(self, *args, **kwargs):
        data = self.request.data
        currency_obj = self.get_object()

        data['name'] = currency_obj.name
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
