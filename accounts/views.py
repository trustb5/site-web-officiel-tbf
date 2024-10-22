from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


def Login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method=='POST':
        if(User.objects.filter(username=username).exists()):
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:dash')
            else:
                messages.error(request, "Mot de passe incorrects! Réessayez")
                return redirect('accounts:login')
        else:
            messages.error(request, "Données incorrects! Réessayez")
            return redirect('accounts:login')
    else:
        return render(request, 'dash/login.html')

@login_required
def Dash(request):
    template_name='dash/dash.html'
    return render(request, template_name)

@login_required
def Logout(request):
    logout(request)
    template_name='dash/login.html'
    return render(request, template_name)