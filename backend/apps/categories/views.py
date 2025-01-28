from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.categories.models import CategoryModel
from apps.categories.serializers import CategorySerializer


class CategoryListCreateView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data

        serializer = CategorySerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
