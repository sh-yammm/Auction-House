from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User


# Create your views here.


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'authentication/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # change to your homepage url name
        else:
            return render(request, 'authentication/login.html', {'error': 'Invalid credentials'})



class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')  # back to login page



class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'authentication/register.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            return render(request, 'accounts/register.html', {'error': 'Passwords do not match'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Username already taken'})

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('home')  # or redirect to login if preferred
