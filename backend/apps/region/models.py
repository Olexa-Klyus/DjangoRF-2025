from django.db import models


class RegionModel(models.Model):
    class Meta:
        db_table = 'regions'

    name = models.CharField(max_length=50)
    value = models.IntegerField()
