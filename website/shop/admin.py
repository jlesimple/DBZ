from django.contrib import admin

from shop.models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')

admin.site.register(Product, ProductAdmin)
