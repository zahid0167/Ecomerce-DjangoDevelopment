from django.urls import path
from .import views

app_name = 'App_payment'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    
 

]
   
