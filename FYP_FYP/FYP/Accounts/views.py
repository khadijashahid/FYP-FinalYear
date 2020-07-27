from django.shortcuts import render, redirect
from .form import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # To grab user from form
            messages.success(request, f'Account was created for' + username)
            return redirect('accounts/login.html')
    else:
        form = CreateUserForm()
    return render(request, 'accounts/register.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def loginUser(request):
    return render(request, "accounts/login.html")

