from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from App_login.models import Profile
from App_login.forms import ProfileForm, SignUpForm

from django.contrib import messages

# Create your views here.

def sign_up(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created Succefully!!!!1")
            return HttpResponseRedirect(reverse('App_login:login'))
    return render(request, 'App_login/signup.html', context={'form':form})


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_shop:home'))
    return render(request, 'App_login/login.html', context={'form':form})



@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "You are Logout.....")
    return HttpResponseRedirect(reverse('App_shop:home'))


@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.user, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, "Changed Saved.....")
            form = ProfileForm(instance=profile)
    return render(request, 'App_login/change_profile.html', context={'form':form})