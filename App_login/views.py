from django.shortcuts import render,redirect ,HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm



def sign_up(request):
    if request.user.is_authenticated:
       return redirect('index')
    form = SignUp()
    reg = False
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            reg = True
    data = {'form':form,'reg':reg}
    return render(request,'al/signup.html',data)


def log_in(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)     
        if user:
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
               return HttpResponse('Incorrect INformation')
        else:
            return HttpResponse('user isnot activae')               
    return render(request,'al/login.html',)

@login_required
def log_out(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    user = request.user

    data = {'user':user}
    return render(request,'al/profile.html',data)

def ChangeProfile(request):
    user = request.user.user_profile
    form = ProfileChange(instance=user)

    if request.method == 'POST':
        form = ProfileChange(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return HttpResponse('incorrect info')
        
    data = {'form':form}
    return render(request,'al/update-profile.html',data)

@login_required
def passChange(request):
    user = request.user
    form = PasswordChangeForm(user)
    if request.method == "POST":
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            return redirect('login')


    data = {'form':form}
    return render(request,'al/cpass.html',data)

