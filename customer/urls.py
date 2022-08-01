from django.urls import path
from . import views
app_name = 'customer'
urlpatterns = [
    path('custhome',views.custhome,name='home'),
    path('viewproduct',views.viewproduct,name="viewproduct"),
    path('productdetail',views.productdetail,name="productdetail"),
    path('orderdetail',views.orderdetail,name="orderdetail"),
    path('cart',views.cart,name='cart'),
]