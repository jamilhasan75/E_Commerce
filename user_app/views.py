from django.shortcuts import render, redirect, HttpResponse
from user_app.forms import RegistrationForm

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form = RegistrationForm()
    return render(request, 'user_app/register.html',{'form':form})

#login page
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('contact_page')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'user_app/login.html')

#logout 
def logout_view(request):
    logout(request)
    return redirect('contact_page')


