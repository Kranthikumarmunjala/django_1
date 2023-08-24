from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=233)

    def __str__(self):
        return str(self.name)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=233)


class Products(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=233)
    price = models.IntegerField()
    description = models.CharField(max_length=233, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return srt(self.id)
