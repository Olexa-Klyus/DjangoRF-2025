from gc import get_objects
from locale import currency

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.currency.models import CurrencyModel, CurrencyPointModel
from apps.currency.serializers import CurrencyPointSerializer


class CurrencyPointUpdateView(GenericAPIView):
    queryset = CurrencyModel.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['patch']

    def patch(self, *args, **kwargs):
        currency_inst = self.get_object()
        data = self.request.data

        if data['ccy'] == "USD":
            data['id'] = 2
        elif data['ccy'] == "EUR":
            data['id'] = 3

        data['saleRate'] = data['buy']
        data['purchaseRate'] = data['sale']

        serializer = CurrencyPointSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


class CurrencyPointCreateView(GenericAPIView):
    queryset = CurrencyPointModel.objects.all()
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data

        if data['ccy'] == "USD":
            data['currency'] = 2
        elif data['ccy'] == "EUR":
            data['currency'] = 3

        data['saleRate'] = data['buy']
        data['purchaseRate'] = data['sale']

        serializer = CurrencyPointSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
