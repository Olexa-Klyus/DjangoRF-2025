from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.city.models import CityModel
from apps.city.serializers import CitySerializer


class CityListCreateView(ListCreateAPIView):
    queryset = CityModel.objects.all()
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)