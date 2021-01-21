

from django.contrib import admin
from products.models import ProductGroup, Family
from products.models import Product

admin.site.register(Product)
admin.site.register(ProductGroup)
admin.site.register(Family)
