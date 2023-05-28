from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('catalog', views.catalog, name='catalog'),
    path('cart/', views.cart, name='cart'),
    path('products/<>', views.product)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

