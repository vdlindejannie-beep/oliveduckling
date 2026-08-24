import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oliveduckling.settings')
django.setup()

from main.models import Product

def seed_database():
    Product.objects.all().delete()

    products = [
        {
            "name": "Custom Quote Canvas Tote Bag",
            "price": 14.99,
            "description": "Durable eco-friendly cotton canvas tote bag customized with high-quality permanent vinyl designs.",
            "image_url": "https://images.unsplash.com/photo-1597484661643-2f5fef640dd1?auto=format&fit=crop&w=600&q=80"
        },
        {
            "name": "Personalized Enamel Mug",
            "price": 12.50,
            "description": "Perfect for camping or cozy mornings. Custom names, quotes, or botanical designs available.",
            "image_url": "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?auto=format&fit=crop&w=600&q=80"
        },
        {
            "name": "Custom Printed Graphic T-Shirt",
            "price": 19.99,
            "description": "Soft, comfortable cotton t-shirt featuring custom heat-transfer vinyl (HTV) graphics.",
            "image_url": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=600&q=80"
        },
        {
            "name": "Handmade Wooden Event Sign",
            "price": 34.99,
            "description": "Custom vinyl lettering on natural finished wood for weddings, baby showers, or home entryway decor.",
            "image_url": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=600&q=80"
        }
    ]

    for item in products:
        Product.objects.create(**item)

    print("Successfully seeded Hello Olive Design Studio products with matching images!")

if __name__ == "__main__":
    seed_database()