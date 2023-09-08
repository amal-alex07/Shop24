# apps.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This apps.py demonstrates the configuration of functions.

from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'product'
    labels = 'my_product'