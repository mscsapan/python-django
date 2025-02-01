from django.shortcuts import render
from django.http import HttpResponse

def my_cart(request):
    return render(request,'cart/cart.html')