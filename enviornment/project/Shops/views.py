from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Shop
from . serializers import ShopSerializer
from math import *

class CreateShopView(generics.CreateAPIView):
  queryset = Shop.objects.all()
  serializer_class = ShopSerializer
  
  
class SearchShopView(APIView):
  def get(self,request):
    user_latitude = request.query_params.get('lat')
    user_longitude = request.query_params.get('lon')
    
    if user_latitude is None or user_longitude is None:
      return Response({"message": "Latitude and longitude must be provided."}, status=400)

    try:
      user_latitude = float(user_latitude)
      user_longitude = float(user_longitude)
    except ValueError:
      return Response({"message": "Latitude and longitude must be valid numbers."}, status=400)
    
    shop = Shop.objects.all() 
    
    shops = [] 
    
    for i in shop:
      distance = self.haversine(user_latitude, user_longitude,i.latitude,i.longitude)
      shops.append((i,distance))
      
    shops.sort(key=lambda x:x[1])
    sorted_shops =[i for i,_ in shops]
    serializer = ShopSerializer(sorted_shops,many = True)
    return Response(serializer.data)
      
      
  @staticmethod  
  def haversine(lat1, lon1, lat2, lon2):
    R = 6371  
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c
    
