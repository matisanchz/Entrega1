from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Entrega1.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contrasenia = form.cleaned_data['password']
            
            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect('libros')
        
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
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

@login_required
def editar_perfil(request):
    usuario = request.user
    
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data['email']
            usuario.password1(data['password1'])
            # usuario.password2 = data['password2']
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.save()
            return redirect('inicio')
    else:
        formulario = UserEditForm({'email': usuario.email})
    
    return render(request, 'editar.html', {'form': formulario})


def about(request):
    return render(request, 'about.html')