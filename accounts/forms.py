from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    """ Defining Login Form attributes """

    username = forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter password'
    }))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your username'
    }), label='Username')

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter new password'
    }), label='Password')

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirm password'
    }), label='Confirm password')