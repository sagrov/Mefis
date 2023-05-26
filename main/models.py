import uuid
from django.contrib.auth.models import User
from django.db import models

from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    img = models.ImageField(upload_to=f"img/category", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Fabric(models.Model):
    name = models.CharField(max_length=100, default="Dynamic")
    color = models.ForeignKey("Color", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name}'


class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Characteristics(models.Model):
    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.fabric}\n{self.size}'


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='products/')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    characteristics = models.ForeignKey(Characteristics, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} --> {self.name}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField("img", upload_to=f"img/%Y/%m/%d/")

    def __str__(self):
        return self.product.name
