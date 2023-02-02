from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomerSerializer, SupplierSerializer, CategorySerializer, UnitSerializer, ProductSerializer, TransactionTypeSerializer, TransactionSerializer
from .models import Customer, Supplier, Category, Unit, Product, TransactionType, Transaction
# from . import models

class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    