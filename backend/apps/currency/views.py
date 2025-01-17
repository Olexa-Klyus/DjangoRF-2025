from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.currency.models import CurrencyPointModel
from apps.currency.serializers import CurrencyPointSerializer


class CurrencyPointListCreateView(ListCreateAPIView):
    queryset = CurrencyPointModel.objects.all()
    serializer_class = CurrencyPointSerializer
    permission_classes = (AllowAny,)
