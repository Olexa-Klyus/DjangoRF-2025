from unicodedata import category

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.car_mark.models import CarMarkModel
from apps.car_mark.serializers import CarMarkSerializer
from apps.categories.models import CategoryModel


class CarMarkListCreateView(ListCreateAPIView):
    queryset = CarMarkModel.objects.all()
    serializer_class = CarMarkSerializer
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarMarkSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)

        pk = kwargs['pk']

        category_obj = CategoryModel.objects.get(pk=pk)
        serializer.save(category=category_obj)
        return Response(serializer.data, status.HTTP_200_OK)
