from main.models import Product, Expense

Product.objects.get_or_create(
    name="Elegante 'Geboorte' Raamsticker",
    price=24.95,
    description="Custom vinyl window decal with delicate olive branch wreath and baby details."
)

Product.objects.get_or_create(
    name="'Geslaagd!' Wooden Garden Sign",
    price=44.95,
    description="Handcrafted lawn sign with custom vinyl text, designed to hold the flag and school bag."
)

Product.objects.get_or_create(
    name="Milestone Birthday Entrance Board",
    price=39.95,
    description="Arch-shaped sign for 21, 30, Sara/Abraham 50 celebrations."
)

Expense.objects.get_or_create(
    title="Matte Sage Vinyl Roll (10m)",
    cost=34.50,
    category="Materials"
)

Expense.objects.get_or_create(
    title="Wooden Garden Board Blank x5",
    cost=62.00,
    category="Materials"
)

print("Database seeded with Dutch celebration products and demo expenses successfully.")