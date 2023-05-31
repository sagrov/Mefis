from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='home'),
                  path('catalog', views.catalog, name='catalog'),
                  path('category/<int:category_id>', views.category, name='category_details'),
                  path('cart', views.cart, name='cart'),
                  path('products/<int:product_real_id>', views.product, name='product_page'),
                  path('add_to_cart', views.add_to_cart, name='add'),
                  path("remove_from_cart", views.remove_from_cart, name="remove"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
