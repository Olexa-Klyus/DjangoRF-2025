from django.db import models

from core.models import BaseAdminModel


class AutoSalonModel(BaseAdminModel):
    class Meta:
        db_table = 'auto_salons'

    name = models.CharField(max_length=100)
