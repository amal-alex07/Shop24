# views.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This views.py demonstrates the core logic of the web application resides. 


from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .serializers import *
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import User
from shop24 import settings
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
)



class UserList(viewsets.ModelViewSet):
    """
    List of all user's ...!
    """

    queryset = User.objects.all().order_by('-id')
    serializer_class = UserListSerializer



class UserRegistration(CreateAPIView):

    authentication_classes = ()
    permission_classes = []
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        email = request.data['email'].strip().lower()
        password = request.data['password'].strip()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer.save()

        """
        Set User password and generate the token for the user.
        """
        user = serializer.instance
        user.set_password(password)
        token, created = Token.objects.get_or_created(user=user)
        user.save()
        data = serializer.data
        data['token'] = token.key


        return Response({
            'success': True,
            'data': request.data,
            'msg': 'user registration successfully..!!!'
        })


class UserLoginView(APIView):
    """
    Creating User Log-in.
    """

    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
   
    def post (self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializers.validate_data['user']
        token, created = Token.objects.get_or_created(user=user)
        content = {
            'token': unicode(token.key)
        }

        return Response(content)