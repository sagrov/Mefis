from django.shortcuts import render, get_object_or_404
from .models import (Categories, Subcategories,
                     Product, ProductImage,
                     Size, Fabric,
                     Cart, CartItem, ProductForMainPage)


def index(request):
    categories = Categories.objects.all()
    products = Product.objects.all()
    products_six = ProductForMainPage.objects.all()
    return render(request, 'main/index.html', {'products': products, 'products_six': products_six, 'categories': categories })


def catalog(request):
    # if request.method == "GET":
    #     request_category = request.GET.get("category")
    #     request_subcategory = request.GET.get("subcategory")
    #     if request.GET.get("category"):
    #         if request_category == "Стільці":
    #             products = Product.objects.filter(category=2)
    #         elif request_category == "Столи":
    #             products = Product.objects.filter(category=3)
    #         elif request_category == "Лампи":
    #             products = Product.objects.filter(category=4)
    #         elif request_category == "Ліжка":
    #             products = Product.objects.filter(category=5)
    #         elif request_category == "Дивани":
    #             products = Product.objects.filter(category=6)
    #         else:
    #             products = Product.objects.all()
    #
    #     if request.GET.get("subcategory"):
    #         if request_subcategory == "Домашні":
    #             products = Product.objects.filter(subcategory=2)
    #         if request_subcategory == "Офісні":
    #             products = Product.objects.filter(subcategory=3)
    #         if request_subcategory == "Всі товари":
    #             products = Product.objects.all()
    categories = Categories.objects.all()
    products = Product.objects.filter(category=request.GET.get("category"))
    print(request.GET.get("category"))
    subcategories = Subcategories.objects.all()
    return render(request, 'main/catalog.html', {'products': products, 'categories': categories, 'subcategories': subcategories})

def category(request, category_id):
    categories = Categories.objects.all()
    products = Product.objects.filter(category__product__id=category_id)
    print(request.GET.get("category"))
    subcategories = Subcategories.objects.all()
    return render(request, 'main/catalog.html', {'products': products, 'categories': categories, 'subcategories': subcategories})


def cart(request):
    return render(request, 'main/cart.html')


def product(request):
    if request.method == "GET":
        request_name = request.GET.get("name")
        product = get_object_or_404(Product, name=request_name)
        products = Product.objects.all()
        product_images = product.productimage_set.all()
        # product_main_images = ProductImage.objects.filter(product=product)
    return render(request, 'main/product.html', {'product_main': product, 'products': products, 'product_images': product_images})

