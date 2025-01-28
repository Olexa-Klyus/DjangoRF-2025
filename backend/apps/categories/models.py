from django.db import models


class CategoryModel(models.Model):
    class Meta:
        db_table = 'categories'

    name = models.CharField(max_length=50)
    value = models.IntegerField()



