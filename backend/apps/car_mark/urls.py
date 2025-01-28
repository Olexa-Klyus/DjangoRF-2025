from django.urls import path

from .views import CarMarkListCreateView

urlpatterns = [
    path('/categories/<int:pk>/marks', CarMarkListCreateView.as_view()),
]
