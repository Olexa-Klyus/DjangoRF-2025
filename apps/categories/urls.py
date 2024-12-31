from django.urls import path

from .views import CategoryCreateArrayView, CategoryListCreateView

urlpatterns = [
    path('/categories', CategoryListCreateView.as_view()),
    path('/categories/array', CategoryCreateArrayView.as_view()),
]
