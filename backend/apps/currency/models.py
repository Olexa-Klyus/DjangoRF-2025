from django.db import models

from core.models import BaseModel


class CurrencyModel(models.Model):
    class Meta:
        db_table = 'currency'

    name = models.CharField(max_length=5)
    desc = models.CharField(max_length=20)


class CurrencyPointModel(BaseModel):
    class Meta:
        db_table = 'currency_point'
        ordering = ['-date_point']

    date_point = models.DateField(auto_now_add=True)
    currency = models.ForeignKey(CurrencyModel, on_delete=models.CASCADE, null=True, related_name='currency_point')
    saleRate = models.DecimalField(decimal_places=7, max_digits=12, null=True)
    purchaseRate = models.DecimalField(decimal_places=7, max_digits=12, null=True)
    saleRateNB = models.DecimalField(decimal_places=7, max_digits=12, null=True)
