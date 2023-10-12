from django.contrib import admin

from .models import (Customer, Order, OrderItem, Product, ShippingAddress,
                     review)

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(review)
