from rest_framework import serializers

from .models import Customer, Supplier, Category, Unit, Product, TransactionType, Transaction

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name','mobile','credit_limit', 'created_at', 'updated_at')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'name','mobile','rep_name', 'rep_mobile', 'created_at', 'updated_at')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name','created_at', 'updated_at')

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name', 'created_at', 'updated_at')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'unit', 'category', 'supplier', 'selling_price', 'cost_price', 'created_at', 'updated_at')

class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ('id', 'name', 'created_at', 'updated_at')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'name', 'price', 'quantity', 'discount','amount', 'notes','is_bounced', 'created_at', 'updated_at')