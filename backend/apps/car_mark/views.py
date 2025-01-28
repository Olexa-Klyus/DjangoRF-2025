from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.car_mark.models import CarMarkModel
from apps.car_mark.serializers import CarMarkSerializer


class CarMarkListCreateView(ListCreateAPIView):
    queryset = CarMarkModel.objects.all()
    serializer_class = CarMarkSerializer
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data

        serializer = CarMarkSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
