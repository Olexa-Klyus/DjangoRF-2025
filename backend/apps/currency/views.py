from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.currency.models import CurrencyModel, CurrencyPointModel
from apps.currency.serializers import CurrencySerializer


class CurrencyPointCreateView(GenericAPIView):
    queryset = CurrencyModel.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data
        context_ = {"name": data["ccy"], "saleRate": data["buy"], "purchaseRate": data["sale"]}

        serializer = CurrencySerializer(data=data, context=context_)
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
        context_ = {"name": data["ccy"], "saleRate": data["buy"], "purchaseRate": data["sale"]}

        serializer = CurrencySerializer(currency_obj, data=data, context=context_)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        CurrencyPointModel.objects.create(currency=CurrencyModel.objects.get(name=serializer.data['name']),
                                          saleRate=serializer.data['saleRate'],
                                          purchaseRate=serializer.data['purchaseRate'],
                                          )

        return Response(serializer.data, status.HTTP_200_OK)
