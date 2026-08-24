from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

class CustomOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    event_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.customer_name}"

class Expense(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - €{self.cost}"