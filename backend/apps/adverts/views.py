from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.pagination import AdvertsListPagination

from apps.adverts.filters import AdvertsFilters
from apps.adverts.models import AdvertModel
from apps.adverts.serializers import AdvertCreateSerializer, AdvertGetInfoSerializer, AdvertPhotoSerializer, \
    AdvertAutoSalonSerializer


class AdvertCreateView(CreateAPIView):
    queryset = AdvertModel.objects.all()
    serializer_class = AdvertCreateSerializer


class AdvertGetAllView(ListAPIView):
    queryset = AdvertModel.objects.all()
    serializer_class = AdvertGetInfoSerializer
    pagination_class = AdvertsListPagination
    filterset_class = AdvertsFilters
    permission_classes = (AllowAny,)


class AdvertGetInfoView(RetrieveAPIView):
    queryset = AdvertModel.objects.all()
    serializer_class = AdvertGetInfoSerializer
    permission_classes = (IsAuthenticated,)


class AdvertRetrieveUpdateDestroyView(GenericAPIView):
    queryset = AdvertModel.objects.all()
    http_method_names = ['get', 'put', 'delete']

    def get(self, *args, **kwargs):
        advert = self.get_object()

        serializer = AdvertGetInfoSerializer(advert)

        return Response(serializer.data, status.HTTP_200_OK)


class AdvertAddPhotoView(UpdateAPIView):
    serializer_class = AdvertPhotoSerializer
    queryset = AdvertModel.objects.all()
    http_method_names = ['put']

    def perform_update(self, serializer):
        advert = self.get_object()
        advert.photo.delete()
        super().perform_update(serializer)


class AdvertAddAutoSalonView(UpdateAPIView):

    def get_queryset(self):
        user = self.request.user
        # group = Group.objects.create(name='salon Mazda2')
        group = Group.objects.get(name='salon Mazda2')

        group.permissions.add(25, 26, 27, 28)
        # print(group.permissions.all())

        user.groups.add(group)
        if user.has_perm('advertmodel.change_advertmodel'):
            print('has permission!!!')

        # user.user_permissions.add(41, 42, 43, 44)
        # print(user.user_permissions.all())
        # if user.has_perm('auto_salon.add_autosalonmodel'):
        #     print('has permission!!!')

        return AdvertModel.objects.filter(user_id=self.request.user.id)

    permission_classes = (IsAuthenticated,)
    serializer_class = AdvertAutoSalonSerializer

    http_method_names = ['patch']
