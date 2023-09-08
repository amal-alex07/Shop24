# url.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This url.py demonstrates the routing configuration for the web application. 


from django.urls import path, include
from rest_framework import routers
from product import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductListViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'payment', views.PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
