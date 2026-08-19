from django.contrib import admin
from .models import Product, CustomOrder, Expense

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(CustomOrder)
class CustomOrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'event_date', 'status', 'created_at')
    list_filter = ('status', 'event_date')
    search_fields = ('customer_name', 'email', 'details')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'category', 'date')
    list_filter = ('category', 'date')