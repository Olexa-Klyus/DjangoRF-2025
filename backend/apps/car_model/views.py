from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from apps.car_mark.models import CarMarkModel
from apps.car_model.models import CarModelModel
from apps.car_model.serializers import CarModelSerializer
from apps.user.permissions import IsAdminOrReadOnly


class CarModelListCreateView(ListCreateAPIView):
    queryset = CarModelModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def post(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs['pk']

        serializer = CarModelSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        mark_obj = CarMarkModel.objects.get(pk=pk)
        serializer.save(car_mark=mark_obj)

        return Response(serializer.data, status.HTTP_200_OK)

