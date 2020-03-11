from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

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

class Rating(models.Model):
     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)] )
     class Meta:
          unique_together = (( 'user', 'movie'), )
          index_together = (('user', 'movie'), )
