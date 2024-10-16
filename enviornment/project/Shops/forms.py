from django import forms
from .models import Shop

class Shopform(forms.ModelForm):
  class Meta:
    model = Shop
    fields = ('name', 'latitude', 'longitude')
    