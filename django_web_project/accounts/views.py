from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

from .forms import RegistrationForm, LoginForm


def registration(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
        else:
            messages.error(request, f'Error')
            return redirect('registration')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'registration.html', context=context)


class Login(LoginView):
    template_name = 'login.html'
    redirect_field_name = 'home_app:home'
    authentication_form = LoginForm
    redirect_authenticated_user = True
    #context_object_name = 'form'


# Create your views here.
