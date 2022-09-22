from django.shortcuts import render
from django.http import HttpResponse

from shop.models import Product

def index(request):
    return render(request, 'shop/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render (request, 'shop/product_detail.html', {'product': product})

def add_to_cart(request, id):
    user = request.user
    product = Product.object.get(id=id)
    
