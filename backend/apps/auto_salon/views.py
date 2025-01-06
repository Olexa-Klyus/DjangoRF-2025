from rest_framework.generics import ListCreateAPIView

from apps.auto_salon.models import AutoSalonModel
from apps.auto_salon.serializers import AutoSalonSerializer


class AutoSalonListCreateView(ListCreateAPIView):
    queryset = AutoSalonModel.objects.all()
    serializer_class = AutoSalonSerializer

