from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from apps.city.models import CityModel
from apps.city.serializers import CitySerializer
from apps.region.models import RegionModel
from apps.user.permissions import IsAdminOrReadOnly


class CityListCreateView(ListCreateAPIView):
    queryset = CityModel.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = CityModel.objects.filter(region_id=pk)
        return queryset

    def post(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs['pk']

        serializer = CitySerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        region_obj = RegionModel.objects.get(pk=pk)
        serializer.save(region=region_obj)

        return Response(serializer.data, status.HTTP_201_CREATED)
