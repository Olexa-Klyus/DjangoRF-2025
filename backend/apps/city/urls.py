from django.urls import path

from .views import CityListCreateView

urlpatterns = [
    path('/states/<int:pk>/cities', CityListCreateView.as_view()),
]
