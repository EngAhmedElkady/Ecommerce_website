from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["prod_name","prod_cost"]
    list_filter = ('prod_price',) 
    
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductAlternative)
admin.site.register(ProductAccessores)

