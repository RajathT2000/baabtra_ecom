from django.shortcuts import render

# Create your views here.
def custhome(request):
    return render(request,'customer/custhome.html')

def viewproduct(request):
    return render(request,'customer/viewproduct.html')

def productdetail(request):
    return render(request,'customer/productdetail.html')

def orderdetail(request):
    return render(request,'customer/orderdetail.html')

def cart(request):
    return render(request,'customer/cart.html')

