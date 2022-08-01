from django.urls import path

from . import views 
app_name = 'common'
urlpatterns = [
    path('',views.index,name='index'),
    path('cust_signup',views.cust_signup,name='cust_signup'),
    path('cust_login',views.cust_login,name='cust_login'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('reseller_signup',views.reseller_signup,name='reseller_signup'),
    path('reseller_login',views.reseller_login,name='reseller_login'),
]