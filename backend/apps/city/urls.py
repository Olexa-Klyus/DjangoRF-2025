from django.urls import path

from .views import CityListCreateView

urlpatterns = [
    path('/regions/<int:pk>/cities', CityListCreateView.as_view()),
]
