from django.shortcuts import render
from .models import (Categories, Subcategories,
                     Product, ProductImage,
                     Size, Fabric,
                     Cart, CartItem, ProductForMainPage)


def index(request):
    products = ProductForMainPage.objects.all()
    return render(request, 'main/index.html', {'products': products})


def catalog(request):
    _type = request.GET.get('office', 'home')
    products = Product.objects.all()
    categories = Categories.objects.all()
    subcategories = Subcategories.objects.all()
    return render(request, 'main/catalog.html', {'product': products, 'categories': categories, 'subcategories': subcategories})


def cart(request):
    return render(request, 'main/cart.html')


def product(request):
    return render(request, 'main/product.html')
