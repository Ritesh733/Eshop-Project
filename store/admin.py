from django.contrib import admin
from .models.product import Product
from .models.category import Category


# Register your models here.

# @admin.register(Product)  ##### by this also can register model


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


# @admin.register(Category)    ##### by this also can register model


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
