from django.urls import path

from apps.adverts.views import AdvertCreateView, AdvertGetAllView, AdvertGetInfoView, AdvertRetrieveUpdateDestroyView

urlpatterns = [
    path('/used/autos', AdvertCreateView.as_view()),
    path('/search', AdvertGetAllView.as_view()),
    path('/info/<int:pk>', AdvertGetInfoView.as_view()),
]
