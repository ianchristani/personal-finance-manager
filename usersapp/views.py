from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# user not loged in page
def index(request):
    return render(request, 'index.html')

# registering page
def signup_view(request):
    if request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        # registering and login in the user
        if signupForm.is_valid():
            validatedUser = signupForm.save()
            login(request, validatedUser)
            return redirect('crud:eventList')
    else:
        signupForm = UserCreationForm()
    return render(request, 'signup.html', {'signupform': signupForm})
    

# login page
def login_view(request):
    if request.method == "POST":
        authForm = AuthenticationForm(data = request.POST)
        # loging in the user
        if authForm.is_valid():
            validatedUser = authForm.get_user()
            login(request, validatedUser)
            return redirect('crud:eventList')
    else:
        authForm = AuthenticationForm()
    return render(request, 'login.html', {'authform': authForm})
    

# logout page
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('usersapp:index')
    else:
        return render(request, 'logout.html')