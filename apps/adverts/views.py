from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from core.pagination import AdvertsListPagination

from apps.adverts.filters import AdvertsFilters
from apps.adverts.models import AdvertModel
from apps.adverts.serializers import AdvertCreateSerializer, AdvertGetInfoSerializer


class AdvertCreateView(CreateAPIView):
    queryset = AdvertModel.objects.all()
    serializer_class = AdvertCreateSerializer


class AdvertGetAllView(ListAPIView):
    queryset = AdvertModel.objects.all()
    serializer_class = AdvertGetInfoSerializer
    pagination_class = AdvertsListPagination
    filterset_class = AdvertsFilters


class AdvertGetInfoView(RetrieveAPIView):
    queryset = AdvertModel.objects.all()
    serializer_class = AdvertGetInfoSerializer


class AdvertRetrieveUpdateDestroyView(GenericAPIView):
    queryset = AdvertModel.objects.all()

    def get(self, *args, **kwargs):
        advert = self.get_object()

        serializer = AdvertGetInfoSerializer(advert)

        return Response(serializer.data, status.HTTP_200_OK)
