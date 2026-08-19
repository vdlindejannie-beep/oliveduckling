from django.urls import path
from . import views

urlpatterns = [
    path('', views.storefront, name='storefront'),
    path('dashboard/', views.dashboard_overview, name='dashboard'),
]