from django.urls import path

from .views import CityListCreateView

urlpatterns = [
    path('/auto/states/<int:pk>/cities', CityListCreateView.as_view()),
]
