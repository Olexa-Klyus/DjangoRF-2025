from json import JSONDecoder

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.currency.models import CurrencyPointModel
from apps.currency.serializers import CurrencyPointSerializer


class CurrencyPointListCreateView(ListCreateAPIView):
    queryset = CurrencyPointModel.objects.all()
    serializer_class = CurrencyPointSerializer
    permission_classes = (AllowAny,)


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
