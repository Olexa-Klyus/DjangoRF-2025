from django.urls import path

from .views import RegionListCreateView

urlpatterns = [
    path('/regions', RegionListCreateView.as_view()),

]
