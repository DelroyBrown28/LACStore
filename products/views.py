from django.shortcuts import render
from .models import Product


def home(request):
    if request.user.is_authenticated:
        username_is = "Delroy"
        context = {"username_is": request.user}
    else:
        context = {"username_is": request.user}

    template = 'products/home.html'
    return render(request, template, context)
    

def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all_products.html'
    return render(request, template, context)





