from django.urls import path

from .views import BodyStylesCreateArrayView, BodyStylesListCreateView

urlpatterns = [
    path('/bodystyles', BodyStylesListCreateView.as_view()),
    path('/bodystyles/array', BodyStylesCreateArrayView.as_view()),
]
