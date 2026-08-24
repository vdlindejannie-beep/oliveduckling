from django.shortcuts import render
from .models import Product

DEFAULT_PRODUCTS = [
    {
        "name": "Botanische Emaille Campingmok",
        "price": 12.50,
        "description": "Lichte en duurzame emaille mok gepersonaliseerd met botanische illustraties en naam.",
        "image_url": "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "Gepersonaliseerde Katoenen Tote Bag",
        "price": 14.99,
        "description": "Stevige milieuvriendelijke katoenen draagtas bedrukt met een eigen quote of naam in premium vinyl.",
        "image_url": "https://images.unsplash.com/photo-1597484661643-2f5fef640dd1?auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "Custom Bedrukt Katoenen T-Shirt",
        "price": 19.99,
        "description": "Zacht 100% biologisch katoenen shirt met op maat gesneden vinyl bedrukking naar keuze.",
        "image_url": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "Houten Welkomstbord Bruiloft / Event",
        "price": 34.99,
        "description": "Handgemaakt houten bord met strakke witte vinyl belettering voor feesten of bruiloften.",
        "image_url": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "Matzwarte RVS Drinkfles",
        "price": 17.50,
        "description": "Dubbelwandige roestvrijstalen thermobeker met gepersonaliseerde naamopdruk.",
        "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?auto=format&fit=crop&w=600&q=80"
    }
]

def home_view(request):
    if request.method == "POST":
        return render(request, "home.html", {"submitted": True})
    return render(request, "home.html")

def shop_view(request):
    # Automatically add default items if the shop table is empty
    if not Product.objects.exists():
        for item in DEFAULT_PRODUCTS:
            Product.objects.create(**item)

    products = Product.objects.all()
    return render(request, "shop.html", {"products": products})