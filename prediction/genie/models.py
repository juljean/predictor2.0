from django.db import models
import datetime
from django.utils import timezone


class CryptBD(models.Model):
    date = models.CharField(max_length=15)
    close = models.DecimalField(max_digits=20, decimal_places=2)
    volume_BT = models.DecimalField(max_digits=20, decimal_places=2)
    volume_USD = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return str(self.date)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)