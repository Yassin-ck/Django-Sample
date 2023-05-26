from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Offer,Sales
# Create your views here. 

def index(request):
    products = Product.objects.all()
    sales = Sales.objects.all()
    return render(request,'index.html',{'productss':products,'saless':sales})
    # return  HttpResponse('<h1>Product Page</h1>')
def offers(request):
    offers = Offer.objects.all() 
    return render(request,'offers.html',{'offerss':offers})
    # return HttpResponse('<h1>About Page</h1>')
def contact(request):
    return render(request,'index2.html')
