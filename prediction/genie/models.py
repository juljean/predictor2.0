from django.db import models
from genie.auto_update import df_records

# Abstract class for all coins

class CryptBD(models.Model):
    date = models.CharField(max_length=10)
    close = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        abstract = True

# Bitcoin model

class BtcBD(CryptBD):
    def __str__(self):
        return str(self.date)

# Ethereum model

class EthBD(CryptBD):
    def __str__(self):
        return str(self.date)


# For the data-uploading(

# model_instances = [BtcBD(
#     date=record[('Date', 'BTC-USD')],
#     close=record[('Close', 'BTC-USD')],
# ) for record in df_records]
# BtcBD.objects.bulk_create(model_instances)


