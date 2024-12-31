from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.categories.models import CategoryModel
from apps.categories.serializers import CategorySerializer


class CategoryListCreateView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateArrayView(GenericAPIView):
    queryset = CategoryModel.objects.all()

    def post(self, *args, **kwargs):
        data = self.request.data
        arr = []
        for item in data:
            serializer = CategorySerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            arr.append(serializer.data)

        return Response(arr, status.HTTP_200_OK)
