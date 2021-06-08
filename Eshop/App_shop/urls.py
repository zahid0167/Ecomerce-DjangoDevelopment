from django.urls import path
from App_shop import views

app_name = 'App_shop'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('catagory/', views.category_show, name='category'),
    path('detail/<pk>/', views.ProductDetails.as_view(), name='product_detail'),
]
