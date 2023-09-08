# serializer.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This serializer.py demonstrates to convert Django models or Python dictionaries.

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from shop24 import settings
from django.db.models.fields import EmailField
from django.core.validators import validate_email


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'user_name',
            'email',
            'role',
        )
        
        

        extra_kwargs = {
            'id': {
                'read_only': True,
                'required': False,
            }
        }


    def create(self, validate_data):
        """
        Create custom method to handle many to many relationship
        """

        instance = super(UserListSerializer, self).create(validate_data)
        if instance.initial_login:
            reset_password(instance.email)

        return instance


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Creating User Registration Serializer 
    """

    password = serializers.CharField(
    style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = (
            'email',
            'user_name',
            'role',
            'password',
        )

    @staticmethod
    def validate_email(value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email alredy exits.")
        return value
    
    @staticmethod
    def validate_password(value):
        if len(value) <getattr(settings, 'PASSWORD_MIN_LENGTH', 4):
            raise serializers.ValidationError(
                    "Password should be atleast %s characters long." % getattr(settings, 'PASSWORD_MIN_LENGTH', 4)
        )


class UserLoginSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    password = serializers.CharField(
    style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )

    def validate(self, attrs, validate_data):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            if validate_email(email):
                user_request = get_objects_or_404(
                    User, 
                    email=email,
                )
                email = user_request.email

            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = "User is not Active"
                    raise Exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given Credentials"
                raise Exceptions.ValidationError(msg)
        else:
            msg = "must include email and password"
            raise Exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs
