from django.contrib import admin
from .models import Brand, Category, Product

# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category')
    fields = ('name', 'description', 'is_digital', 'price', 'brand', 'category')


admin.site.register(Product, ProductAdmin)
