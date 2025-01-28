from django.urls import path

from .views import CarModelListCreateView

urlpatterns = [
    path('/categories/<int:id>/marks/<int:pk>/models', CarModelListCreateView.as_view()),

]
