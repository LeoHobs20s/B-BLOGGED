from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm
from django.views import View


class LoginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, self.template_name, {'form':form})


def logout_view(request):
    """ Logging user out """
    logout(request)
    return redirect('login_view')


class RegistrationView(View):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = new_user.username
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                user.save()
                login(request, user)
                return redirect('index')
        return render(request, self.template_name, {'form':form})
      