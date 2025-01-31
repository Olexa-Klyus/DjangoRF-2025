from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from better_profanity import profanity

from core.pagination import AdvertsListPagination

from apps.adverts.filters import AdvertsFilters
from apps.adverts.models import AdvertModel
from apps.adverts.serializers import (
    AdvertAutoSalonSerializer,
    AdvertCreateUpdateSerializer,
    AdvertGetInfoSerializer,
    AdvertGetUserAutosSerializer,
    AdvertPhotoSerializer,
    AdvertSearchSerializer,
)
from apps.adverts.services import get_avg_prices
from apps.auto_salon.models import AutoSalonModel
from apps.car_mark.models import CarMarkModel
from apps.car_model.models import CarModelModel
from apps.visits_count.services import get_visit_count, visit_add


class AdvertCreateView(GenericAPIView):
    queryset = AdvertModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        data = self.request.data
        user = self.request.user

        context_ = {'price_init': data['price']}

        if 'car_mark' in data:
            mark_obj = get_object_or_404(CarMarkModel, value=data['car_mark'])
            context_['car_mark'] = mark_obj

        if 'car_model' in data:
            model_obj = get_object_or_404(CarModelModel, value=data['car_model'])
            context_['car_model'] = model_obj

        adverts_count = self.queryset.filter(user_id=self.request.user.id).count()

        if not user.profile.premium_acc and adverts_count:
            return Response(f'account is premium = {user.profile.premium_acc},'
                            f' adverts_count = {adverts_count}'
                            , status.HTTP_403_FORBIDDEN)

        if profanity.contains_profanity(data["description"]):
            serializer = AdvertCreateUpdateSerializer(data=data, context=context_)
            serializer.is_valid(raise_exception=True)
            serializer.save(user_id=user, is_active=False, profanity_edit_count=1)

            return Response(f'Oголошення не активне, містить ненормативну лексику. Є 3 спроби на виправлення',
                            status.HTTP_403_FORBIDDEN)

        serializer = AdvertCreateUpdateSerializer(data=data, context=context_)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=user, is_active=True)

        return Response(serializer.data, status.HTTP_201_CREATED)


class AdvertUpdateView(GenericAPIView):
    queryset = AdvertModel.objects.filter(is_visible=True)
    permission_classes = (IsAuthenticated,)
    http_method_names = ['patch', ]

    def patch(self, *args, **kwargs):
        advert = self.get_object()
        data = self.request.data
        context_ = {}

        if 'car_mark' in data:
            mark_obj = get_object_or_404(CarMarkModel, value=data['car_mark'])
            context_['car_mark'] = mark_obj

        if 'car_model' in data:
            model_obj = get_object_or_404(CarModelModel, value=data['car_model'])
            context_['car_model'] = model_obj

        if profanity.contains_profanity(data["description"]):
            advert.is_active = False
            if advert.profanity_edit_count < 3:
                advert.profanity_edit_count += 1
                advert.save()
                return Response(
                    f'Oголошення містить ненормативну лексику. Залишилось {4 - advert.profanity_edit_count} спроби',
                    status.HTTP_403_FORBIDDEN)
            else:
                advert.is_visible = False
                advert.save()
                return Response(f'Oголошення заблоковане. Зверніться до адміна сайту', status.HTTP_403_FORBIDDEN)

        serializer = AdvertCreateUpdateSerializer(advert, data=data, context=context_, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(is_active=True, profanity_edit_count=0)

        return Response(serializer.data, status.HTTP_200_OK)


class AdvertGetInfoView(GenericAPIView):
    queryset = AdvertModel.objects.all()
    http_method_names = ['get']
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        advert = self.get_object()
        user = self.request.user

        # додали перегляд до лічильника
        visit_add(self.request, advert.id)

        # додали до instans лічильники
        advert.counter = get_visit_count(advert.id, user)

        # додали до instans середні ціни
        advert.avg_prices = get_avg_prices(advert, user)

        advert.created_at = advert.created_at.strftime("%m/%d/%Y, %H:%M:%S")
        advert.updated_at = advert.updated_at.strftime("%m/%d/%Y, %H:%M:%S")

        serializer = AdvertGetInfoSerializer(advert)
        return Response(serializer.data, status.HTTP_200_OK)


class AdvertSearchView(ListAPIView):
    queryset = AdvertModel.objects.filter(is_active=True, is_visible=True)
    serializer_class = AdvertSearchSerializer
    pagination_class = AdvertsListPagination
    filterset_class = AdvertsFilters
    permission_classes = (AllowAny,)


class AdvertGetUserAutosView(ListAPIView):
    queryset = AdvertModel.objects.filter(is_visible=True)
    serializer_class = AdvertGetUserAutosSerializer
    pagination_class = AdvertsListPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user_id=user.id)
        return queryset

# class AdvertGetByIdView(RetrieveAPIView):
#     queryset = AdvertModel.objects.filter(is_visible=True)
#     serializer_class = AdvertGetByIdSerializer
#     permission_classes = (IsAuthenticated,)
#     http_method_names = ['get']


        # obj_perm = UserObjectPermission.objects.assign_perm(user_or_group=user, perm='change_advertmodel',
        #                                                     obj=(AdvertModel.objects.get(id=25)))
        #
        # if user.has_perm('change_advertmodel', obj=(AdvertModel.objects.get(id=25))):
        #     print(f'{user.profile.name} has permission change_group {AdvertModel.objects.get(id=25)}')
        # else:
        #     print('RFHGJBKJNLKJ:J:JL:JI')
        #
        # # print(obj_perm)




class AdvertAddPhotoView(UpdateAPIView):
    serializer_class = AdvertPhotoSerializer
    queryset = AdvertModel.objects.filter(is_active=True, is_visible=True)
    http_method_names = ['put']

    def perform_update(self, serializer):
        advert = self.get_object()
        advert.photo.delete()
        super().perform_update(serializer)


class AdvertAddAutoSalonView(UpdateAPIView):
    queryset = AdvertModel.objects.filter(is_active=True, is_visible=True)
    permission_classes = (AllowAny,)
    serializer_class = AdvertAutoSalonSerializer

    def get_queryset(self):
        user = self.request.user
        # obj_perm = UserObjectPermission.objects.assign_perm('change_group', user, obj=group2)

        # group1 = Group.objects.get(name='salon Mazda')
        # group2 = Group.objects.get(name='salon Mazda2')
        if user.has_perm(80):
            print(f'{user.profile.name} has permission 80')

        print(user.user_permissions.all())
        print(user.groups.all())
        print(user.get_group_permissions())
        content_type = ContentType.objects.get_for_model(AutoSalonModel)

        # if user.has_group_permissions(80):
        #     print(f'{user.profile.name} has permission 80')
        # print(user.group_permissions.all())

        group = Group.objects.get_or_create(name='salon Mazda2')

        group.permissions.add(25, 26, 27, 28)
        # print(group.permissions.all())

        user.groups.add(group)
        if user.has_perm('advertmodel.change_advertmodel'):
            print('has permission!!!')

        return AdvertModel.objects.all()

    # if user.has_perm('change_group', group2):
    #     print(f'{user.profile.name} has permission change_group {group2.name}')
    # else:
    #     print(f'{user.profile.name} has not permission change_group {group2.name}')
    #
    # if user.has_perm('change_group', group1):
    #     print(f'{user.profile.name} has permission change_group {group1.name}')
    # else:
    #     print(f'{user.profile.name} has not permission change_group {group1.name}')
    #
    # if user.has_perm('change_group'):
    #     print(f'{user.profile.name} has permission change_group all groups')
    # else:
    #     print(f'{user.profile.name} has not permission change_group all groups')

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

    # return AdvertModel.objects.filter(user_id=self.request.user.id)

    # def get_queryset(self):
    #     queryset = self.queryset.filter(user_id=self.request.user.id)
    #
    #     user = self.request.user
    #     obj_perm = UserObjectPermission.objects.assign_perm(user_or_group=user, perm='change_advertmodel',
    #                                                         obj=(AdvertModel.objects.get(id=25)))
    #
    #     if user.has_perm('change_advertmodel', obj=(AdvertModel.objects.get(id=25))):
    #         print(f'{user.profile.name} has permission change_group {AdvertModel.objects.get(id=25)}')
    #     else:
    #         print('RFHGJBKJNLKJ:J:JL:JI')
    #
    #     # print(obj_perm)
    #
    #     return queryset
