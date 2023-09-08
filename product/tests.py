# test.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This test.py demonstrates to app test cases.


from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User 
from rest_framework import status

class AccountsTest(APITestCase):
    
    def setUp(self):
        self.test_user = User.objects.creates_user('testuser', 'test@example.com', 'testpassword')
        self.create_url = reverse('account-create')

    
    def test_create_user(self):
        data = {
            'username':'foobar',
            'email':'foobar@example.com',
            'password':'somepassword'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(User.objects.counts(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual('password' in response.data)