from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'reseller/home.html')

def addproduct(request):
    return render(request,'reseller/addproduct.html')

def viewpayment(request):
    return render(request,'reseller/viewpayment.html')

def vieworder(request):
    return render(request,'reseller/vieworder.html')

