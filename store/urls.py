from django.urls import path
from store import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('products/', views.product_list, name='product_list'),
    #path('product/', views.product_detail, name='product_detail'),
    #path('cart/', views.cart, name='cart'),
   # path('checkout/', views.checkout, name='checkout'),
]
