from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

from .forms import RegistrationForm


def registration(request):
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


#def login(request):


# Create your views here.
