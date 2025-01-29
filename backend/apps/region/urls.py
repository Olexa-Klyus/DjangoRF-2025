from django.urls import path

from .views import RegionListCreateView

urlpatterns = [
    path('/states', RegionListCreateView.as_view()),

]
