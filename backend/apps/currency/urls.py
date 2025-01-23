from django.urls import path

from .views import CurrencyPointUpdateView

urlpatterns = [
    path('/currency_point_add/<str:name>', CurrencyPointUpdateView.as_view())
]
