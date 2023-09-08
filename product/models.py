# model.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This model.py demonstrates the data structure and schema of a database.


from django.db import models
from accounts.models import User
from django.utils import timezone



class Product(models.Model):

    BOX = 'BX'
    BOTTLE = 'BL'

    CHOICES = (
        (BOX, 'box'),
        (BOTTLE, 'bottle'),
    )
    
    product_name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    packing_type = models.CharField(max_length=2, choices=CHOICES, default=BOX)
    packing_quantity = models.IntegerField()
    price_to_retailer = models.DecimalField(max_digits=10, decimal_places=2)
    price_to_seller = models.DecimalField(max_digits=10, decimal_places=2)
    msrp = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(default=timezone.now)
    edited_on = models.DateTimeField(auto_now=True)



class Cart(models.Model):

    product = models.ForeignKey(Product, related_name='cart_product', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, related_name='cart_user', on_delete=models.CASCADE)
    count = models.IntegerField(default=1, blank=True, null=True)
    initial_count = models.IntegerField(default=1, blank=True, null=True)
    save_or_later = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)
    edited_on = models.DateTimeField(auto_now=True)



class Payment(models.Model):

    STATUSES = (
        ('SD', 'Shipped'),
        ('PD', 'Pending'),
        ('OD', 'OutForDelivery'),
        ('PO', 'PaymentDone'),
        ('CT', 'Cart'),
        ('AP', 'Approved'),
        ('PL', 'PayLater'),
        ('DL', 'Delivered'),
    )

    PAYMENT_METHOD = (
        ('NP', 'NotPaid'),
        ('OP', 'OnlinePayment'),
        ('CP', 'CashPayment'),
        ('QP', 'ChequePayment'),
    )

    cart = models.ManyToManyField(Cart, related_name='product_cart', blank=True)
    status = models.CharField(max_length=2, choices=STATUSES, default='PD')
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHOD, default='NP')
    payment_date = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    edited_on = models.DateTimeField(auto_now=True)

    