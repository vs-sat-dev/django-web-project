from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=32,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(label='Email', max_length=254,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password', max_length=32,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Password confirm', max_length=32,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))
    terms_of_service = forms.BooleanField(label='Terms of service', required=True, disabled=False,
                                          widget=forms.CheckboxInput(
                                              attrs={'class': 'form-check-label', 'align': 'left'}
                                          ))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'terms_of_service')

        """widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
        }"""


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=64,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password', max_length=32,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class ProfileChangeForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput())
    email = forms.EmailField(label='Email', max_length=254,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    bio = forms.CharField(label='Bio',
                          widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bio'}))

    class Meta:
        model = CustomUser
        fields = ('image', 'email', 'bio')
