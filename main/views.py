from django.shortcuts import render
from django.db.models import Sum
from .models import Product, CustomOrder, Expense

def storefront(request):
    products = Product.objects.all()
    submitted = False
    
    if request.method == 'POST':
        CustomOrder.objects.create(
            customer_name=request.POST.get('name'),
            email=request.POST.get('email'),
            event_date=request.POST.get('event_date') or None,
            details=request.POST.get('details'),
            reference_file=request.FILES.get('reference_file')
        )
        submitted = True
    
    return render(request, 'store.html', {'products': products, 'submitted': submitted})

def dashboard_overview(request):
    orders = CustomOrder.objects.all().order_by('-created_at')
    expenses = Expense.objects.all().order_by('-date')
    total_expenses = Expense.objects.aggregate(Sum('cost'))['cost__sum'] or 0
    return render(request, 'dashboard.html', {
        'orders': orders, 
        'expenses': expenses,
        'total_expenses': total_expenses
    })