
from django.shortcuts import render

from .models import Product


# Create your views here.
def product(request, id):
    products=Product.objects.get(id=id)
    context={
        'products':products
    }
    return render(request,'products/product.html',context);

def products(request):
    return render(request,'products/products.html',{'pro':Product.objects.all()});


