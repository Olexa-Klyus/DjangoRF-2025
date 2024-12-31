from django.db import models

from core.models import BaseAdminModel


class CategoryModel(BaseAdminModel):
    class Meta:
        db_table = 'categories'

    name = models.CharField(max_length=50)
    value = models.IntegerField()
