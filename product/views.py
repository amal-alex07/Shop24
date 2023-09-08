# views.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This views.py demonstrates the core logic of the web application resides. 


from django.shortcuts import render
from django.http import HttpResponse
from shop24 import settings
from rest_framework import viewsets
from .models import *
from .serializers import *

from rest_framework.response import Response 
from rest_framework import status


class ProductListViewSet(viewsets.ModelViewSet):
    """
    Listing all products..

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class CartViewSet(viewsets.ModelViewSet):
    """
    View for add items to Cart...!!

    """

    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    View for payment items

    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
