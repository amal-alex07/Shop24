# admin.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This admin.py demonstrates the admin functions.


from django.contrib import admin

# Register your models here.
from product.models import Product
from product.models import Cart
from product.models import Payment


admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Payment)