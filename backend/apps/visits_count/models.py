from django.db import models


class VisitCountModel(models.Model):
    class Meta:
        db_table = 'visit_count'

    ip = models.CharField(max_length=50)
    user = models.IntegerField(null=True)
    advert = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
