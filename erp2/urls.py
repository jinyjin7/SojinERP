from django.urls import path
from erp2 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inbound/',views.inbound, name='inbound'),
    path('inventory/',views.inventory, name='inventory'),
    path('outbound/',views.outbound, name='outbound'),
    path('product_adding/',views.product_adding, name='product_adding')
    ]