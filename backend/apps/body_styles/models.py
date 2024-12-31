from django.db import models

from core.models import BaseAdminModel


class BodyStylesModel(BaseAdminModel):
    class Meta:
        db_table = 'body_styles'

    name = models.CharField(max_length=50)
    value = models.IntegerField()
    parent_id = models.IntegerField()
    category_id = models.IntegerField()
