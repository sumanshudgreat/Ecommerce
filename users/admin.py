from django.contrib import admin
from .models import Product,Order,Cart,Address,Category
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Address)

