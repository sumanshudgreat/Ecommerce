from django.urls import path

from django.contrib.auth.views import LoginView,LogoutView
from .views import register,homepage,category,product,cart,remove,buy,my_orders,cancel_order,search,search_from_any_page

urlpatterns = [
    path('homepage/product/<int:pk>/',product,name='product'),
    path('homepage/category/<int:pk>/',category,name='category'),
    path('homepage/',homepage,name='homepage'),
    path('register/',register,name='register'),
    path('',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('cart/',cart,name='cart'),
    path('remove/<int:pk>/',remove,name='remove'),
    path('cart/buy/<int:pk>/',buy,name='buy'),
    path('my_orders/',my_orders,name='orders'),
    path('my_orders/<int:pk>/',cancel_order,name='cancel_order'),
    path('search/',search,name='search'),
    path('search_from_any_page/',search_from_any_page,name='search_from_any_page'),
]