from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Register your models here.


@admin.register(Product)  ##### by this also can register model
class AdminProduct(admin.ModelAdmin):
    list_display = ["name", "image", "price", "category"]


@admin.register(Category)  ##### by this also can register model
class AdminCategory(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Customer)  ##### by this also can register model
class AdminCustomer(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email", "phone", "password"]


# admin.site.register(Customer, AdminCustomer)
