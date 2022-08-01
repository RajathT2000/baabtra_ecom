from django.urls import path
from . import views
app_name = 'reseller'
urlpatterns = [
    path('home',views.home,name='home'),
    path('addproduct',views.addproduct,name="addproduct"),
    path('viewpayment',views.viewpayment,name="viewpayment"),
    path('vieworder',views.vieworder,name="vieworder")
]