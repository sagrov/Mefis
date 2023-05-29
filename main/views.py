from django.shortcuts import render, get_object_or_404
from .models import (Categories, Subcategories,
                     Product, ProductImage,
                     Size, Fabric,
                     Cart, CartItem, ProductForMainPage)


def index(request):
    categories = Categories.objects.all()
    products = Product.objects.all()
    products_six = ProductForMainPage.objects.all()
    return render(request, 'main/index.html',
                  {'products': products, 'products_six': products_six, 'categories': categories})


def catalog(request):
    sorting_options = [
        {
            'name': 'Назва',
            'field': 'name'
        },
        {
            'name': 'Ціна',
            'field': 'price'
        },
        {
            'name': 'Категорія',
            'field': 'category'
        },

    ]
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
    categories = Categories.objects.all()
    main_product = Product.objects.get(id=product_real_id)
    main_product_images = ProductImage.objects.filter(main_product=main_product)
    products = Product.objects.all()
    return render(request, 'main/product.html',
                  {'head_product': main_product, 'categories': categories, 'products': products,
                   'head_product_images': main_product_images})


def cart(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    return render(request, 'main/cart.html', {'categories': categories, 'products': products})
