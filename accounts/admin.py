# admin.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This admin.py demonstrates the admin functions.

from django.contrib import admin

from accounts.models import User

admin.site.register(User)