from django.urls import path

from apps.auto_salon.views import AutoSalonListCreateView

urlpatterns = [
    path('/auto_salons', AutoSalonListCreateView.as_view(), name='auto_salon_list_create'),
]
