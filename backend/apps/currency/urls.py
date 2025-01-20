from django.urls import path

from .views import CurrencyPointCreateView, CurrencyPointListCreateView

urlpatterns = [
    path('/currency_point', CurrencyPointCreateView.as_view())
]
