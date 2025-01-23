from django.urls import path

from .views import CurrencyPointCreateView, CurrencyPointUpdateView

urlpatterns = [
    path('/currency_point_add', CurrencyPointUpdateView.as_view())
]
