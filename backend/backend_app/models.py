from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255, null=True)
    credit_limit = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255, null=True)
    rep_name = models.CharField(max_length=255, null=True)
    rep_mobile = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    unit = models.ForeignKey(Unit, related_name="product", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, related_name="products", on_delete=models.CASCADE)
    selling_price = models.DecimalField(max_digits=10, decimal_places=8)
    cost_price = models.DecimalField(max_digits=10, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TransactionType(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, null=True, decimal_places=8)
    quantity = models.DecimalField(max_digits=10, null=True, decimal_places=8)
    discount = models.DecimalField(max_digits=10, default=0, decimal_places=8)
    amount = models.DecimalField(max_digits=10, decimal_places=8)
    notes = models.TextField(null=True)
    is_bounced = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name