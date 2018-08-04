from django.db import models
from django_pandas.managers import DataFrameManager
# Create your models here.


class Bovespa(models.Model):
    Ticker = models.CharField(max_length=7)
    Date = models.DateField()
    Open = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    High = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    Low = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    Close = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    Volume = models.IntegerField()
    objects = models.Manager()
    pdobjects = DataFrameManager()  # Pandas-Enabled Manager
    class Meta:
        unique_together = ['Ticker','Date']



    def __str__(self):
        return self.Ticker



class Document(models.Model):
    description = models.CharField(max_length=255, blank=False)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description



class TICKER(models.Model):
    Ticker = models.CharField(max_length=7)



    def __str__(self):
        return self.Ticker
