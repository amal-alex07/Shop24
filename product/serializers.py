# serializer.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This serializer.py demonstrates to convert Django models or Python dictionaries.


from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *

from accounts.serializers import UserListSerializer




class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for List all Products.!!!
    """

    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for add items to cart..!!!
    """

    user_details = UserListSerializer(source='user', read_only=True)
    product_details = ProductSerializer(source='product', read_only=True, required=False)
    
    class Meta:
        model = Cart
        fields = (
            'id',
            'product',
            'user',
            'count',
            'save_or_later',
            'product_details',
            'user_details',
            'created_on',
            'initial_count',
        )

        extra_kwargs = {
            'id': {
                'read_only': True,
                'required': False,
            }}
        


class PaymentSerializer(serializers.ModelSerializer):
    """
    Serialiser for Payment to added items in Cart.!!
    """

    # cart = CartSerializer(source='carts', read_only=True)
    cart = Cart.objects.all()
    # total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = (
            'id',
            'cart',
            'status',
            'payment_id',
            'payment_method',
            'cart',
            # 'total_cost',
            'created_on',
            'payment_date',
        )
