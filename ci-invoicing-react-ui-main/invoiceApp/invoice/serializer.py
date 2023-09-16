from rest_framework import serializers
from .models import *


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ["desc","rate","quantity"]



class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemsSerializer(many=True)
    
    class Meta:
        model = Invoice
        fields = "__all__"
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
