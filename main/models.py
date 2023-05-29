import uuid
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    # slug = models.SlugField(max_length=100, unique=True, default=uuid.uuid4())

    def __str__(self):
        return f'{self.name}'


class Subcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    # slug = models.SlugField(max_length=100, db_index=True, unique=True, default=uuid.uuid4())

    def __str__(self):
        return f'{self.name}'


class Size(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'name: {self.name}\n'


class Fabric(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    addition_to_price = models.IntegerField(default=0)

    def __str__(self):
        return f'name: {self.name}\naddition_to_price: {self.addition_to_price}\n '


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # slug = models.SlugField(max_length=100, db_index=True, unique=True, default=uuid.uuid4())

    fabrics = models.ForeignKey(Fabric, on_delete=models.DO_NOTHING, null=True)

    photo = models.ImageField(upload_to='main/static/main/img')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(Subcategories, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} --> {self.name}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.ImageField("img", upload_to='main/static/main/img')

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        items = self.cartitems.all()
        total = sum([item.price for item in items])
        return total

    @property
    def count(self):
        items = self.cartitems.all()
        quantity = sum([item.quantity for item in items])
        return quantity


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product.name)

    @property
    def price(self):
        return self.product.price * self.quantity


class ProductForMainPage(models.Model):
    name = models.CharField(max_length=50)
    pic = models.FileField("img", upload_to='main/static/main/img')

    def __str__(self):
        return f'{self.name} --> {self.pic}'