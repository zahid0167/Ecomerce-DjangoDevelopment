from django.urls import path
from .import views

app_name = 'App_order'

urlpatterns = [
    path('add/<pk>/', views.add_to_cart, name='add'),
    path('cart/', views.cart_view, name='cart'),
    path('increase/<pk>/', views.increase_item, name='increase'),
    path('decrese/<pk>/', views.decrese_item, name='decrese'),
    path('remove/<pk>/', views.remove_item, name='remove'),
]
