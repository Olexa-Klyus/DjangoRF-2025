from django.urls import path

from .views import CarModelListCreateView

urlpatterns = [
    path('/categories/<int:pk>/marks/<int:pk>/models', CarModelListCreateView.as_view()),

]
