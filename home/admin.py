from django.contrib import admin
from .models import Product,Offer,Sales

class ProductAdmin(admin.ModelAdmin):
        list_display = ('name','stock','price')
class OfferAdmin(admin.ModelAdmin):
        list_display = ('code','discount')
class SalesAdmin(admin.ModelAdmin):
        list_display = ('sale','damage')
# Register your models here.

admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(Sales,SalesAdmin)