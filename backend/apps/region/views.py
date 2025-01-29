from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from apps.region.models import RegionModel
from apps.region.serializers import RegionSerializer
from apps.user.permissions import IsAdminOrReadOnly


class RegionListCreateView(ListCreateAPIView):
    queryset =RegionModel.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def post(self, *args, **kwargs):
        data = self.request.data

        serializer = RegionSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
