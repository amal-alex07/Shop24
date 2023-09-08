# test.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This test.py demonstrates to app test cases.


import json


# from models import User
# from django.contrib.auth.models import User

from django.urls import reverse


# from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase




class UserRegistrationAPIViewTestCase(APITestCase):
    
    url = reverse("accounts:regi")

    def test_invalid_password(self):
        pass

    



# if __name__ == "__main__":
#     main()    +
