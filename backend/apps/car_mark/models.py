from django.db import models

from apps.categories.models import CategoryModel


class CarMarkModel(models.Model):
    class Meta:
        db_table = 'car_marks'

    name = models.CharField(max_length=50)
    value = models.IntegerField()

    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='car_marks')