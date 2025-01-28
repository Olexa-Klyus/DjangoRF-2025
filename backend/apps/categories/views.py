from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from apps.categories.models import CategoryModel
from apps.categories.serializers import CategorySerializer
from apps.user.permissions import IsAdminOrReadOnly


class CategoryListCreateView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)

    def post(self, *args, **kwargs):
        data = self.request.data

        serializer = CategorySerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
