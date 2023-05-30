from django.contrib import admin
from .models import *

admin.site.register(Categories)
admin.site.register(Subcategories)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Size)
admin.site.register(Fabric)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ProductForMainPage)
admin.site.register(Colors)