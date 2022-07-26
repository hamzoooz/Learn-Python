from django.shortcuts import render
from .models import  Product

# Create your views here.

def product(request):
    return render(request, 'products/product.html', { 'pro' : Product.objects.all()} )


def products(request):
    a = Product.objects.all()
    # c =  Product.objects.count()
    # a = Product.objects.all().filter(price=100)
    # return render(request, 'products/products.html', {'name':'Hamzoooz'})
    return render(request, 'products/products.html',  {'pro' : a } , { 'count':  Product.objects.count()})
    # return render(request, 'products/products.html',  { 'count':  Product.objects.count() })



