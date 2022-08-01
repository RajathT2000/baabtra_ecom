from django.shortcuts import render

def index(request):
    return render(request,'common/projecthome.html')

def cust_signup(request):
    return render(request,'common/cust_signup.html')

def cust_login(request):
    return render(request,'common/cust_login.html')

def admin_login(request):
    return render(request,'common/admin_login.html')

def reseller_signup(request):
    return render(request,'common/reseller_signup.html')

def reseller_login(request):
    return render(request,'common/reseller_login.html')

