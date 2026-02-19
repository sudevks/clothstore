from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def product_list(request):
    return render(request, 'product_list.html')

def product_detail(request):
    return render(request, 'product_detail.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')
