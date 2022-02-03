from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=32,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(label='Email', max_length=64,
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
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'terms_of_service')

        """widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
        }"""


class LoginForm(forms.ModelForm):
    model = User
    template_name = 'login.html'
    success_url = 'home.html'

    class Meta:
        fields = ['email', 'password']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }
