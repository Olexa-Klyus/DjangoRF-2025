from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.body_styles.models import BodyStylesModel
from apps.body_styles.serializers import BodyStylesSerializer


class BodyStylesListCreateView(ListCreateAPIView):
    queryset = BodyStylesModel.objects.all()
    serializer_class = BodyStylesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class BodyStylesCreateArrayView(GenericAPIView):
    queryset = BodyStylesModel.objects.all()

    def post(self, *args, **kwargs):
        data = self.request.data
        arr = []

        for item in data:
            if 'category_id' in self.request.query_params:
                item['category_id'] = int(self.request.query_params['category_id'])
            item['parent_id'] = item['parentId']
            serializer = BodyStylesSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            arr.append(serializer.data)

        return Response(arr, status.HTTP_200_OK)
