from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from App_order.models import Cart, Order
from App_shop.models import Product
from django.contrib import messages

# Create your views here.
@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity was Updated,,,")
            return redirect("App_shop:home")
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "This item was added your Cart")
            return redirect("App_shop:home")
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, "This item was added your cart")
        return redirect('App_shop:home')

@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)

    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'App_order/cart.html', context={'carts':carts, 'order':order})
    else:
        messages.warning(request, "You dont have any item inyour cart")
        return redirect("App_shop:home")

@login_required
def increase_item(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order= order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                return HttpResponse("Increase your item")


@login_required
def decrese_item(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order= order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity -= 1
                order_item.save()
                return HttpResponse("Decrese your item")

@login_required

def remove_item(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Order.objects.filter(user=request.user, ordered=False)
    if order_item.exists():
        order = order_item[0]
        if order.orderitems.filter(item=item).exists():
            cart_item=Cart.objects.filter(user=request.user, purchased=False)[0]
            cart_item.delete()
            return HttpResponse("Remove your item")

