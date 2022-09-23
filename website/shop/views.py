from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse

from shop.models import Product, Cart, Order

def index(request):
    return render(request, 'shop/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', context={'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render (request, 'shop/product_detail.html', context={'product': product})

def add_to_cart(request, id):
    user = request.user
    product = get_object_or_404(Product, id=id)
    cart, _ = Cart.objects.get_or_create(user=user) # '_' convention ; on recupère juste le panier, utilisé qu'une seul fois
    order, created = Order.objects.get_or_create(user=user, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product-detail", kwargs={"id": id}))
