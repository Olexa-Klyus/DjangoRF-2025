from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.car_model.models import CarModelModel
from apps.car_model.serializers import CarModelSerializer


class CarModelListCreateView(ListCreateAPIView):
    queryset = CarModelModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data

        serializer = CarModelSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

