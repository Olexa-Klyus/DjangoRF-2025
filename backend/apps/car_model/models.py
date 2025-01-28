from django.db import models

from apps.car_mark.models import CarMarkModel


class CarModelModel(models.Model):
    class Meta:
        db_table = 'car_models'

    name = models.CharField(max_length=50)
    value = models.IntegerField()

    car_mark = models.ForeignKey(CarMarkModel, on_delete=models.SET_DEFAULT, default=1, related_name='car_models')
