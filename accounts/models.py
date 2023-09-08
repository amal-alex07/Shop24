# model.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This model.py demonstrates the data structure and schema of a database..

import hashlib


from shop24 import settings
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
# from django.db import Q
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token




class UserManager(BaseUserManager):
    """
    Custom Base Manager for custom User Model. Provides all the functionalities for the AUTH_USER_MODEL.
    """

    use_in_migrations = True


    def _create_user(self, email, password, **kwargs):
        """
        Function to create a user with given arguments
        """
        if not email:
            raise ValueError('User must have a Valid Email address.!')
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **kwargs)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    
    def create_user(self, email, password=None, **kwargs):
        """
        Top level function which call to be upon when a user is to be created.
        """
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    
    def create_superuser(self, email, password, **kwargs):
        """
        Function to create a superuser with all permissions.
        """

        user = self._create_user(email, password, **kwargs)
        user.set_password(password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


    def create(self, **kwargs):
        """
        Override model's create method inoredr to provide better integration with testing
        utilities like mixer, pytest and command level user creation.
        """

        email = kwargs.pop('email', None)
        password = kwargs.pop('password')
        user = self.create_user(email, password)
        user.set_password(password)
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return user

    
    def get_by_email(self, email):
        """
        Returns the user with the email provided.
        """
        return self.get_queryset().get(email=email)

    def _check_unique_email(self, email):
        """
        Checks whether a given email is unique or not.
        Raises validation error when email is already existing, else return True.
        """
        try:
            self.get_queryset().get(email=email)
            raise ValueError("This email is already registered.")
        except self.model.DoesNotExist:
            return True



class User(AbstractBaseUser, PermissionsMixin):

    """
    Extending the Django User Model...
    """

    ROLE_CHOICES  = (
        ('SU', 'Superuser'),
        ('RT', 'Retailer'),
        ('CT', 'Customer'),
    )

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(_('user name'), max_length=25, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    initial_login = models.BooleanField(default=True)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default='CT')
   

    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return str(self.email)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Creating auth token for when a user is created..!
    """
    if created:
        Token.objects.create(user=instance)
        password = instance.password
        instance.set_password(password)
        instance.save()


def perform_destroy(self, instance):
    instance.delete()

