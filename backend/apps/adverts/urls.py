from django.urls import path

from apps.adverts.views import (
    AdvertAddAutoSalonView,
    AdvertAddPhotoView,
    AdvertCreateView,
    AdvertGetInfoView,
    AdvertGetUserAutosView,
    AdvertSearchView,
    AdvertUpdateView,
)

urlpatterns = [
    path('/used/autos', AdvertCreateView.as_view()),
    path('/used/autos/<int:pk>', AdvertUpdateView.as_view()),
    path('/user/autos', AdvertGetUserAutosView.as_view()),
    path('/user/auto/<int:pk>', AdvertGetUserAutosView.as_view()),
    path('/search', AdvertSearchView.as_view()),
    path('/info/<int:pk>', AdvertGetInfoView.as_view()),
    path('/<int:pk>/photos', AdvertAddPhotoView.as_view()),
    path('/<int:pk>/add_auto_salon', AdvertAddAutoSalonView.as_view()),
]
