from django.urls import path

from .views import CurrencyPointListCreateView

urlpatterns = [
    path('/currency_point', CurrencyPointListCreateView.as_view())
]
