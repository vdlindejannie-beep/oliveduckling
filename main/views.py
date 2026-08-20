from django.shortcuts import render
from .models import Product

def home_view(request):
    if request.method == "POST":
        # Process custom inquiry form submissions if needed
        return render(request, "home.html", {"submitted": True})
    return render(request, "home.html")

def shop_view(request):
    products = Product.objects.all()
    return render(request, "shop.html", {"products": products})