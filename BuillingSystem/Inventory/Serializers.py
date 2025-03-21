from rest_framework import serializers
from .models import *

class Products_Serializers(serializers.ModelSerializer):

    class Meta:

        model = Products
        fields = '__all__'

class Products_Serializers2(serializers.ModelSerializer):

    class Meta:

        model = Products
        fields = ['products_name']        