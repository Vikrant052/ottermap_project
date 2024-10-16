from django.urls import path
from .views import CreateShopView, SearchShopView

urlpatterns = [
    path('', CreateShopView.as_view(), name='create_shop'),
    path('search/', SearchShopView.as_view(), name='search_shop'),
]
