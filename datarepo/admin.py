from django.contrib import admin
from .models import Category, SubCategory, Products


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

# class ProductsAdmin(admin.ModelAdmin):


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Products)
