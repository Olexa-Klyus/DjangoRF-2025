from unicodedata import category

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.car_mark.models import CarMarkModel
from apps.car_mark.serializers import CarMarkSerializer
from apps.categories.models import CategoryModel
from apps.user.permissions import IsAdminOrReadOnly


class CarMarkListCreateView(ListCreateAPIView):
    queryset = CarMarkModel.objects.all()
    serializer_class = CarMarkSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = CarMarkModel.objects.filter(category_id=pk)
        return queryset

    def post(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs['pk']

        serializer = CarMarkSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        category_obj = CategoryModel.objects.get(pk=pk)
        serializer.save(category=category_obj)

        return Response(serializer.data, status.HTTP_201_CREATED)
