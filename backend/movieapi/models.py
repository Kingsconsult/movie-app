from django.db import models

class Movie(models.Model):
     STATUSES = (
          ('UNKNOWN', 'unknown'),
          ('FREE', 'free'),
          ('PAID', 'paid')
     )
     title = models.CharField(max_length=36,  unique=True, null=True)
     description = models.TextField(max_length=256, blank=True)
     subscription_type = models.CharField(max_length=9, choices=STATUSES)
     price = models.DecimalField(max_digits=1000, decimal_places=2, default=0)
     published_date = models.DateField(blank=True, null=True, default=None)
     cover = models.ImageField(upload_to='covers/')
