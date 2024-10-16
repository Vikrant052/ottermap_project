from django.db import models
from django.core.exceptions import ValidationError

class Shop(models.Model):
  name = models.CharField(max_length=50)
  latitude = models.FloatField()
  longitude = models.FloatField()
  
  def __str__(self):
    return self.name
  

