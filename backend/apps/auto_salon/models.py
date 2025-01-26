from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

UserModel = get_user_model()


class AutoSalonModel(BaseModel):
    class Meta:
        db_table = 'auto_salons'

    is_visible = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    user_id = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    profanity_edit_count = models.IntegerField(default=0)
