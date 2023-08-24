"""point_sale_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from datarepo.views import add_category, list_category, update_category, delete_category, add_subcategory, \
    list_subcategory, update_subcategory, delete_subcategory, add_products, list_products, update_products, \
    delete_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_category/', add_category, name='add_category'),
    path('list_category/', list_category, name='list_category'),
    path('update_category/', update_category, name='update_category'),
    path('delete_category/', delete_category, name='delete_category'),
    path('add_subcategory/', add_subcategory, name='add_subcategory'),
    path('list-subcategory/', list_subcategory, name='list_subcategory'),
    path('update_subcategory/', update_subcategory, name='update_subcategory'),
    path('delete_subcategory/', delete_subcategory, name='delete_subcategory'),
    path('add_products/', add_products, name='add_products'),
    path('list_products/', list_products, name='list_products'),
    path('update_products/', update_products, name='update_products'),
    path('delete_products/', delete_products, name='delete_products'),
]
