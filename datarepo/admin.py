from django.contrib import admin
from .models import Category, SubCategory, Products


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_filter = ['category']
    search_fields = ['id']


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subcategory', 'price', 'description', 'created_at', 'updated_at']
    list_filter = ['name']
    search_fields = ['id']


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Products, ProductsAdmin)
