from django.shortcuts import render

# Create your views here.
def adminhome(request):
    return render(request,'ecomadmin/adminhome.html')

def approvesellers(request):
    return render(request,'ecomadmin/approvesellers.html')

def viewsellers(request):
    return render(request,'ecomadmin/viewsellers.html')

def viewcustomers(request):
    return render(request,'ecomadmin/viewcustomers.html')
