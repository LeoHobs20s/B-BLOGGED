from django import forms

class LoginForm(forms.Form):
    """ Defining Login Form attributes """

    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

