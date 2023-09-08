# url.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This url.py demonstrates the routing configuration for the web application. 


from django.urls import path, include
from rest_framework import routers
from accounts.views import *


app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'users',UserList, base_name='users'),

urlpatterns = [
    path('', include(router.urls)),
    path('regi/', UserRegistration.as_view(), name='regi'),
    path('login/', UserLoginView.as_view(), name='login'),
]
