from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    """ Logging in user """

    if request.method != 'POST':
        # No Data Submitted; create blank form
        form = LoginForm()
    else:
        # POST Data Submitted; process credentials
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username.title()}')
                return redirect('index')
            else:
                messages.error(request, 'Invalid credentials')
            
    context  = {'form':form}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    """ Logging user out """
    logout(request)
    return redirect('login_view')


def register(request):
    """ Registering users """

    if request.method != 'POST':
        # No Data Submitted; create blank form
        form = UserCreationForm()
    else:
        # POST Data Submitted; process data
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, user)
            return redirect('index')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)  