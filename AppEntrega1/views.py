from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppEntrega1.forms import AvatarFormulario
from Entrega1.forms import UserRegisterForm, UserEditForm
from .models import Avatar, Sucursal, Seccion, Libro, Usuario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user)
        if avatares:
            avatar_url = avatares.last().imagen.url
        else:
            avatar_url = ''
        return render (request, 'home.html', {'avatar_url': avatar_url})
    return render (request, 'home.html')

def sucursal(request):
    return render(request, 'AppEntrega1/sucursal.html', {'sucursales': Sucursal.objects.all()})

def seccion(request):
    return render(request, 'AppEntrega1/seccion.html', {'secciones': Seccion.objects.all()})

def libro(request):
    return render(request, 'AppEntrega1/libro.html', {'libros': Libro.objects.all()})

@login_required
def usuario(request):
    return render(request, 'AppEntrega1/usuario.html', {'usuarios': Usuario.objects.all()})

#Forms Sucursal:
class SucursalListView(ListView):
    model = Sucursal
    template_name = 'AppEntrega1/sucursal.html'
    context_object_name = 'sucursales'

class SucursalDetailView(DetailView):
    model = Sucursal
    template_name = 'AppEntrega1/ver_sucursal.html'

class SucursalCreateView(LoginRequiredMixin, CreateView):
    model = Sucursal
    success_url = reverse_lazy('sucursales')
    fields = ['nombre', 'direccion', 'localidad']
    template_name = 'AppEntrega1/sucursales_form.html'
    
class SucursalUpdateView(LoginRequiredMixin, UpdateView):
    model = Sucursal
    success_url = reverse_lazy('sucursales')
    fields = ['nombre', 'direccion', 'localidad']
    template_name = 'AppEntrega1/sucursales_form.html'

class SucursalDeleteView(LoginRequiredMixin, DeleteView):
    model = Sucursal
    success_url = reverse_lazy('sucursales')

#Forms Seccion:
class SeccionListView(ListView):
    model = Seccion
    template_name = 'AppEntrega1/seccion.html'
    context_object_name = 'secciones'

class SeccionDetailView(DetailView):
    model = Seccion
    template_name = 'AppEntrega1/ver_seccion.html'

class SeccionCreateView(LoginRequiredMixin, CreateView):
    model = Seccion
    success_url = reverse_lazy('secciones')
    fields = ['nombre', 'piso']
    template_name = 'AppEntrega1/secciones_form.html'
class SeccionUpdateView(LoginRequiredMixin, UpdateView):
    model = Seccion
    success_url = reverse_lazy('secciones')
    fields = ['nombre', 'piso']
    template_name = 'AppEntrega1/secciones_form.html'

class SeccionDeleteView(LoginRequiredMixin, DeleteView):
    model = Seccion
    success_url = reverse_lazy('secciones')
    #Por default usa el template seccion_confirm_delete.html

# Forms Libro:
class LibroListView(ListView):
    model = Libro
    template_name = 'AppEntrega1/libro.html'
    context_object_name = 'libros'

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'AppEntrega1/ver_libro.html'

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    success_url = reverse_lazy('libros')
    fields = ['titulo', 'autor', 'fecha_publicacion', 'editorial', 'disponibilidad', 'sitio_oficial']
    template_name = 'AppEntrega1/libros_form.html'
    
class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    success_url = reverse_lazy('libros')
    fields = ['titulo', 'autor', 'fecha_publicacion', 'editorial', 'disponibilidad', 'sitio_oficial']
    template_name = 'AppEntrega1/libros_form.html'
    
class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy('libros')
    #Por default usa el template libro_confirm_delete.html

# Forms Usuario:
class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'AppEntrega1/usuario.html'
    context_object_name = 'usuarios'

class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'AppEntrega1/ver_usuario.html'

class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    success_url = reverse_lazy('usuarios')
    fields = ['nombre', 'apellido', 'id_socio', 'email']
    template_name = 'AppEntrega1/usuarios_form.html'
    
class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    success_url = reverse_lazy('usuarios')
    fields = ['nombre', 'apellido', 'id_socio', 'email']
    template_name = 'AppEntrega1/usuarios_form.html'
    
class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuarios')
    #Por default usa el template libro_confirm_delete.html

def busqueda_usuario(request):
    return render(request, 'AppEntrega1/busquedaUsuario.html')

def buscar(request):
    id_socio = request.GET["id_socio"]
    
    usuarios = Usuario.objects.filter(id_socio = id_socio)
    
    return render(request, 'AppEntrega1/buscar.html', {'usuarios': usuarios, 'id_socio': id_socio})

def busqueda_libro(request):
    return render(request, 'AppEntrega1/busquedaLibro.html')

def buscar_libro(request):
    titulo = request.GET["titulo"]
    
    libros = Libro.objects.filter(titulo__icontains = titulo)
    
    return render(request, 'AppEntrega1/buscar_libro.html', {'libros': libros, 'libro': titulo})

def busqueda_sucursal(request):
    return render(request, 'AppEntrega1/busquedaSucursal.html')

def buscar_sucursal(request):
    nombre = request.GET["nombre"]
    
    sucursales = Sucursal.objects.filter(nombre__icontains = nombre)
    
    return render(request, 'AppEntrega1/buscar_sucursal.html', {'sucursales': sucursales, 'sucursal': nombre})

def pagina_construccion(request):
    return render(request, "AppEntrega1/p??gina_en_construcci??n.html")

def enviar_email(request):
    
    if request.method=="POST":
        subject=request.POST['asunto']
        message=request.POST['mensaje']+ " | Remitente "+ request.POST['correo']
        email_from= settings.EMAIL_HOST_USER
        recipent_list=["contactoalfaproject@gmail.com"]
        send_mail(subject, message, email_from, recipent_list)
        return redirect('mensajeria/enviado')
    
    return render(request, "AppEntrega1/mensajeria.html")

def email_enviado(request):
    return render(request, "AppEntrega1/email_enviado.html")

@login_required 
def agregar_avatar(request):
    if request.method == 'POST':
        formulario = AvatarFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return redirect('mi_perfil')
    else:
        formulario = AvatarFormulario()
        
    return render(request, 'AppEntrega1/crear_avatar.html', {'form': formulario})

@login_required
def mi_perfil(request):
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user)
        if avatares:
            avatar_url = avatares.last().imagen.url
        else:
            avatar_url = ''
        return render (request, 'AppEntrega1/mi_perfil.html', {'avatar_url': avatar_url})
    return render(request, 'AppEntrega1/mi_perfil.html')

@login_required
def editar_perfil(request):
    usuario = request.user
    
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data['email']
            usuario.password1 = data['password1']
            usuario.password2 = data['password2']
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.save()
            return redirect('mi_perfil')
    else:
        formulario = UserEditForm({'email': usuario.email})
    
    return render(request, 'AppEntrega1/editar.html', {'form': formulario})