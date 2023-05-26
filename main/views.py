from django.shortcuts import render
from .models import (Categories, Subcategories,
                     Product, ProductImage,
                     Size, Fabric,
                     Cart, CartItem, ProductForMainPage)


def index(request):
    products = ProductForMainPage.objects.all()
    return render(request, 'main/index.html', {'products': products})


def catalog(request):
    if request.method == "GET":
        if request.GET.get("category"):
            request_category = request.GET.get("category")
            if request_category == "Стільці":
                products = Product.objects.filter(category=2)
            elif request_category == "Столи":
                products = Product.objects.filter(category=3)
            elif request_category == "Лампи":
                products = Product.objects.filter(category=4)
            elif request_category == "Ліжка":
                products = Product.objects.filter(category=5)
            elif request_category == "Дивани":
                products = Product.objects.filter(category=6)
            else:
                products = Product.objects.all()
        if request.GET.get("subcategory"):
            request_subcategory = request.GET.get("subcategory")
            if request_subcategory == "Домашні":
                products = Product.objects.filter(subcategory=2)
            if request_subcategory == "Офісні":
                products = Product.objects.filter(subcategory=3)
            if request_subcategory == "Всі товари":
                products = Product.objects.all()
        else:
            products = Product.objects.all()
    categories = Categories.objects.all()
    subcategories = Subcategories.objects.all()
    return render(request, 'main/catalog.html', {'product': products, 'categories': categories, 'subcategories': subcategories})


def cart(request):
    return render(request, 'main/cart.html')


def product(request):
    return render(request, 'main/product.html')
