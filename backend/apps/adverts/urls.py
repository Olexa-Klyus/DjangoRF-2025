from django.urls import path

from apps.adverts.views import (
    AdvertAddAutoSalonView,
    AdvertAddPhotoView,
    AdvertCreateView,
    AdvertGetAllView,
    AdvertGetInfoView,
    AdvertGetUsersAutosView,
    AdvertUpdateView,
)

urlpatterns = [
    path('/used/autos', AdvertCreateView.as_view()),
    path('/used/autos/<int:pk>', AdvertUpdateView.as_view()),
    path('/user/autos', AdvertGetUsersAutosView.as_view()),
    path('/search', AdvertGetAllView.as_view()),
    path('/info/<int:pk>', AdvertGetInfoView.as_view()),
    path('/<int:pk>/photos', AdvertAddPhotoView.as_view()),
    path('/<int:pk>/add_auto_salon', AdvertAddAutoSalonView.as_view()),
]
