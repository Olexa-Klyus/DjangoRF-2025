from django.db import models

from apps.region.models import RegionModel


class CityModel(models.Model):
    class Meta:
        db_table = 'cities'

    name = models.CharField(max_length=50)
    value = models.IntegerField()
    region = models.ForeignKey(RegionModel, on_delete=models.SET_NULL, null=True)
