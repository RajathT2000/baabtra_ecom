from django.urls import path
from . import views
app_name = 'ecom'

urlpatterns = [
    path('',views.adminhome,name='home'),
    path('approvesellers',views.approvesellers,name='approvesellers'),
    path('viewsellers',views.viewsellers,name='viewsellers'),
    path('viewcustomers',views.viewcustomers,name='viewcustomers'),
]