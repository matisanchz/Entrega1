from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppEntrega1.models import Avatar
from Entrega1.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required

def login_request(request):
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user)
        if avatares:
            avatar_url = avatares.last().imagen.url
        else:
            avatar_url = ''
        return render (request, 'home.html', {'avatar_url': avatar_url})

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contrasenia = form.cleaned_data['password']
            
            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect('home')
        
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'home.html', {'form': form})
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return HttpResponse(f'Usuario {username} creado correctamente.')
        
    else:
        form = UserRegisterForm()
    
    return render(request, 'registro.html', {'form': form})


def about(request):
    return render(request, 'about.html')