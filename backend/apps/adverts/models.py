from django.core import validators as V
from django.db import models

from core.enums import RegexEnum
from core.models import BaseModel

from apps.categories.models import CategoryModel


class AdvertModel(BaseModel):
    class Meta:
        db_table = 'adverts'

    title = models.CharField(max_length=100, blank=True)

    categories = models.ForeignKey(CategoryModel, on_delete=models.PROTECT)
    brand = models.IntegerField()
    car_model = models.IntegerField()
    year = models.IntegerField(validators=[V.MinValueValidator(1900), V.MaxValueValidator(2025)])
    mileage = models.FloatField()
    boby_style = models.IntegerField()
    region = models.IntegerField()
    city = models.IntegerField()
    price = models.IntegerField()
    currency = models.IntegerField()

    description = models.TextField(blank=True, validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg),
                                                           V.MaxLengthValidator(255)])
    gearbox = models.IntegerField(null=True)
    fuel = models.IntegerField(null=True)

    expired_at = models.DateTimeField(null=True)
    user_id = models.IntegerField(null=True)
