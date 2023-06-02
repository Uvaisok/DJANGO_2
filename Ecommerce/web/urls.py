from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('login',views.login2,name='login'),
    path('sign',views.sign2,name='sign'),
    path('logout', views.logout1,name="logout"),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart'),
    path('checkout', views.checkout,name="checkout"),
    path('placeorder', views.placeorder,name="placeorder"),
    path('confirm', views.confirm,name="confirm"),
]