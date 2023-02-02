# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Customer, Supplier, Category, Unit, Product, TransactionType, Transaction

# create a serializer class
class TodoSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = Todo
        fields = ('id', 'title','description','completed')