from django.db import models

from apps.categories.models import CategoryModel


class CarModelModel(models.Model):
    class Meta:
        db_table = 'car_models'

    name = models.CharField(max_length=50)
    value = models.IntegerField()
    parent_id = models.IntegerField(null=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='brands')