from django.shortcuts import render
from django.views.generic import ListView, DetailView
from App_shop.models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'App_shop/home.html'

class ProductDetails(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_shop/product_detail.html'

def category_show(request):
    cat = Category.objects.all()
    return render(request, "App_shop/category_show.html", context={'cat':cat})
