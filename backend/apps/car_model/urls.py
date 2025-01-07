from django.urls import path

from .views import CarModelCreateArrayView, CarModelListCreateView

urlpatterns = [
    path('/car_models', CarModelListCreateView.as_view()),
    path('/car_models/array', CarModelCreateArrayView.as_view()),
]
