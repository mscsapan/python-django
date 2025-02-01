from django.http import HttpResponse
from django.shortcuts import render

def product(request):
    return render(request,'product/product.html')