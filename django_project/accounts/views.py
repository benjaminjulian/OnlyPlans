from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from accounts.forms import ProfileForm, UserRegistrationForm, CustomAuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.template import RequestContext

# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = '/'
    template_name = 'profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

def indexView(request):
    return render(request,'accounts.html')

@login_required()
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('')
    else:
        form = UserRegistrationForm()
    return render(request,'register.html',{'form':form})

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
