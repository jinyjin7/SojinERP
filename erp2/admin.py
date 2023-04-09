from django.contrib import admin
from .models import ProductModel,Inbound,Inventory,Outbound,Product_adding



# Register your models here.
admin.site.register(ProductModel)
admin.site.register(Inbound)
admin.site.register(Inventory)
admin.site.register(Outbound)
admin.site.register(Product_adding)