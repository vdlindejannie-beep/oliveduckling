from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class CustomOrder(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Review'),
        ('APPROVED', 'Quote Approved'),
        ('IN_PROGRESS', 'In Production'),
        ('COMPLETED', 'Completed'),
    ]
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    event_date = models.DateField(null=True, blank=True, help_text="Date of birth, party, or graduation day")
    details = models.TextField(help_text="Dimensions, text, vinyl choices, color preferences")
    reference_file = models.FileField(upload_to='custom_designs/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.get_status_display()}"

class Expense(models.Model):
    title = models.CharField(max_length=200, help_text="e.g., Green Vinyl Roll, Wooden Garden Stakes")
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=100, default='Materials')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (€{self.cost})"