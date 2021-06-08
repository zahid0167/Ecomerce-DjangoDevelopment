from django.shortcuts import render, HttpResponseRedirect
from App_payment.models import BillingAddress
from App_order.models import Order
from App_payment.forms import BillingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def checkout(request):
    saved_addresh = BillingAddress.objects.get_or_create(user=request.user)
    saved_addresh = saved_addresh[0]
    form = BillingForm(instance=saved_addresh)
    if request.method =="POST":
        form = BillingForm(request.POST, instance=saved_addresh)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_addresh)
            messages.success(request, "Your sipping addresh saving!!!")
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total  =order_qs[0].get_totals()
    return render(request, 'App_payment/checkout.html', context={'form':form, 'order_items':order_items,'order_total':order_total})