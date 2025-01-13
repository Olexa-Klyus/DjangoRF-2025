from django.contrib.auth.models import Group

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from guardian.models import UserObjectPermission

from core.pagination import AdvertsListPagination

from apps.adverts.filters import AdvertsFilters
from apps.adverts.models import AdvertModel
from apps.adverts.serializers import (
    AdvertAutoSalonSerializer,
    AdvertCreateSerializer,
    AdvertGetInfoSerializer,
    AdvertPhotoSerializer,
)


class AdvertCreateView(CreateAPIView):
    queryset = AdvertModel.objects.all()
    serializer_class = AdvertCreateSerializer
    permission_classes = (IsAuthenticated,)


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


class AdvertGetUsersAutosView(GenericAPIView):
    queryset = AdvertModel.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        adverts = self.queryset.filter(user_id=self.request.user.id)
        serializer = AdvertGetInfoSerializer(adverts, many=True)
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

        # obj_perm = UserObjectPermission.objects.assign_perm('change_group', user, obj=group2)

        group1 = Group.objects.get(name='salon Mazda')
        group2 = Group.objects.get(name='salon Mazda2')

        if user.has_perm('change_group', group2):
            print(f'{user.profile.name} has permission change_group {group2.name}')
        else:
            print(f'{user.profile.name} has not permission change_group {group2.name}')

        if user.has_perm('change_group', group1):
            print(f'{user.profile.name} has permission change_group {group1.name}')
        else:
            print(f'{user.profile.name} has not permission change_group {group1.name}')

        if user.has_perm('change_group'):
            print(f'{user.profile.name} has permission change_group all groups')
        else:
            print(f'{user.profile.name} has not permission change_group all groups')

        # # group = Group.objects.create(name='salon Mazda2')
        # group = Group.objects.get(name='salon Mazda2')
        #
        # group.permissions.add(25, 26, 27, 28)
        # # print(group.permissions.all())
        #
        # user.groups.add(group)
        # if user.has_perm('advertmodel.change_advertmodel'):
        #     print('has permission!!!')

        # user.user_permissions.add(41, 42, 43, 44)
        # print(user.user_permissions.all())
        # if user.has_perm('auto_salon.add_autosalonmodel'):
        #     print('has permission!!!')

        return AdvertModel.objects.all()
        # return AdvertModel.objects.filter(user_id=self.request.user.id)

    permission_classes = (AllowAny,)
    serializer_class = AdvertAutoSalonSerializer

    http_method_names = ['patch']
