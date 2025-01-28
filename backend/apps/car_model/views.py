from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.car_model.models import CarModelModel
from apps.car_model.serializers import CarModelSerializer


class CarModelListCreateView(ListCreateAPIView):
    queryset = CarModelModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = (AllowAny,)

