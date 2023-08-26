from django.contrib import messages
from django.shortcuts import redirect, render
from .models import User, Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

# Create your views here.
def profiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    #users = Profile.objects.all()
    users = Profile.objects.filter(name__icontains=search_query)
    #print(users)
    return render(request,'users/users.html',{"users":users})

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request,'users/profile.html',{"profile":profile})

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'username does not exist')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'user or password is wrong')
    return render(request,'users/login_register.html')

def userLogout(request):
    logout(request)
    messages.error(request, 'user logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'user account was created')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error has occurred during registration')
    context = {"page":page, "form":form}
    return render(request, 'users/login_register.html', context)