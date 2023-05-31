import json

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls.base import reverse
from django.shortcuts import render, get_object_or_404
from .models import (Categories, Subcategories,
                     Product, ProductImage,
                     Size, Fabric,
                     Cart, CartItem, ProductForMainPage, Colors)


def index(request):
    categories = Categories.objects.all()
    products = Product.objects.all()
    products_six = ProductForMainPage.objects.all()
    return render(request, 'main/index.html',
                  {'products': products, 'products_six': products_six, 'categories': categories})

def catalog(request):
    products = Product.objects.all()
    if request.method == "GET":
        request_subcategory = request.GET.get("subcategory")
        request_category = request.GET.get("category")
        if request_category != '1':
            if request.GET.get("category"):
                products = Product.objects.filter(category=request_category)
        if request.GET.get("subcategory"):
            products = Product.objects.filter(subcategory=request_subcategory)
    categories = Categories.objects.all()
    subcategories = Subcategories.objects.all()
    print(request.GET)
    return render(request, 'main/catalog.html',
                  {'products': products, 'categories': categories, 'subcategories': subcategories,
                   'sorting_options': sorting_options})

def category(request, category_id):
    categories = Categories.objects.all()
    products = Product.objects.filter(category__product__id=category_id)
    subcategories = Subcategories.objects.all()
    return render(request, 'main/catalog.html',
                  {'products': products, 'categories': categories, 'subcategories': subcategories})


def product(request, product_real_id):
    colors = Colors.objects.all()
    categories = Categories.objects.all()
    main_product = Product.objects.get(id=product_real_id)
    main_product_images = ProductImage.objects.filter(product=main_product)
    print(main_product_images[0].images)
    products = Product.objects.all()
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        context = {'head_product': main_product, 'categories': categories, 'products': products, 'head_product_images': main_product_images, 'colors': colors, "cart": cart}
        return render(request, 'main/product.html', context)
    return render(request, 'main/product.html', {'head_product': main_product, 'categories': categories, 'products': products, 'head_product_images': main_product_images, 'colors': colors})


def cart(request):
    cart = None
    cartitems = []

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()
    print(cartitems)
    context = {"cart": cart, "items": cartitems}
    return render(request, 'main/cart.html', context)


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)
    item_quantity = data["quantity"]

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += item_quantity
        cartitem.save()

    return JsonResponse(product_id, safe=False)

def remove_from_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if cartitem.quantity > 0:
            cartitem.objects.filter(prod)
        cartitem.save()

    return JsonResponse(product_id, safe=False)

def clear_cart(request):
    user = request.user
    CartItem.objects.filter(cart__user=user).delete()
    Cart.objects.filter(user=user).delete()
    return HttpResponseRedirect(reverse("cart"))

def catalog(request):
    products = Product.objects.all()
    if request.method == "GET":
        request_category = request.GET.get("category")
        request_subcategory = request.GET.get("subcategory")
        print('request_subcategory  ', request_subcategory)
        print(request.GET)
        if request_category != '1':
            if request.GET.get("category"):
                products = Product.objects.filter(category=request_category)
        if request_subcategory != '1':
            if request.GET.get("subcategory"):
                products = Product.objects.filter(subcategory=request_subcategory)
    categories = Categories.objects.all()

    subcategories = Subcategories.objects.all()
    return render(request, 'main/catalog.html',
                  {'products': products, 'categories': categories, 'subcategories': subcategories})