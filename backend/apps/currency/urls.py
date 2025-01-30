from django.urls import path

from .views import CurrencyPointListCreateView, CurrencyPointUpdateView

urlpatterns = [
    path('/currency_points', CurrencyPointListCreateView.as_view()),
    path('/currency_point_add/<str:name>', CurrencyPointUpdateView.as_view())
]
