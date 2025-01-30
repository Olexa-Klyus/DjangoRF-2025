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

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = CarModelModel.objects.filter(car_mark_id=pk)
        return queryset

    def post(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs['pk']

        serializer = CarModelSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        car_mark_obj = CarMarkModel.objects.get(pk=pk)
        serializer.save(car_mark=car_mark_obj)

        return Response(serializer.data, status.HTTP_201_CREATED)
