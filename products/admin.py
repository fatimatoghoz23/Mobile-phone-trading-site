from django.contrib import admin

from .models import Product  # لاضافة كلاس البرودكت الموجود في المودل

# Register your models here.
admin.site.register(Product)
