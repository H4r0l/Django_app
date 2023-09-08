from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here

def index(request):
    products = Product.objects.all()
    return render(request,'list_of_products.html', {'products': products})

def get_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'show_product.html', {'product': product})