from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def catalog(request):
    return render(request, 'main/catalog.html')


def cart(request):
    return render(request, 'main/cart.html')

