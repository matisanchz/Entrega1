from django.forms import model_to_dict

from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Sucursal, Seccion, Libro, Usuario

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

def inicio(request):
    return render(request, 'AppEntrega1/inicio.html')

def sucursal(request):
    return render(request, 'AppEntrega1/sucursal.html', {'sucursales': Sucursal.objects.all()})

def seccion(request):
    return render(request, 'AppEntrega1/seccion.html', {'secciones': Seccion.objects.all()})

def libro(request):
    return render(request, 'AppEntrega1/libro.html', {'libros': Libro.objects.all()})

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

class SucursalCreateView(CreateView):
    model = Sucursal
    success_url = reverse_lazy('sucursales')
    fields = ['nombre', 'direccion', 'localidad']
    template_name = 'AppEntrega1/sucursales_form.html'
    
class SucursalUpdateView(UpdateView):
    model = Sucursal
    success_url = reverse_lazy('sucursales')
    fields = ['nombre', 'direccion', 'localidad']
    template_name = 'AppEntrega1/sucursales_form.html'

class SucursalDeleteView(DeleteView):
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

class SeccionCreateView(CreateView):
    model = Seccion
    success_url = reverse_lazy('secciones')
    fields = ['nombre', 'piso']
    template_name = 'AppEntrega1/sucursales_form.html'
    #Puedo usar el mismo template que SucursalesCreateView
class SeccionUpdateView(UpdateView):
    model = Seccion
    success_url = reverse_lazy('secciones')
    fields = ['nombre', 'piso']
    template_name = 'AppEntrega1/sucursales_form.html'
    #Puedo usar el mismo template que SucursalesCreateView

class SeccionDeleteView(DeleteView):
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

class LibroCreateView(CreateView):
    model = Libro
    success_url = reverse_lazy('libros')
    fields = ['titulo', 'autor', 'fecha_publicacion', 'editorial', 'disponibilidad', 'sitio_oficial']
    template_name = 'AppEntrega1/sucursales_form.html'
    #Puedo usar el mismo template que SucursalesCreateView
    
class LibroUpdateView(UpdateView):
    model = Libro
    success_url = reverse_lazy('libros')
    fields = ['titulo', 'autor', 'fecha_publicacion', 'editorial', 'disponibilidad', 'sitio_oficial']
    template_name = 'AppEntrega1/sucursales_form.html'
    #Puedo usar el mismo template que SucursalesCreateView
    
class LibroDeleteView(DeleteView):
    model = Libro
    success_url = reverse_lazy('libros')
    #Por default usa el template libro_confirm_delete.html

# Forms Usuario:
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'AppEntrega1/usuario.html'
    context_object_name = 'usuarios'

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'AppEntrega1/ver_usuario.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    success_url = reverse_lazy('usuarios')
    fields = ['nombre', 'apellido', 'id_socio', 'email']
    template_name = 'AppEntrega1/sucursales_form.html'
    #Puedo usar el mismo template que SucursalesCreateView
    
class UsuarioUpdateView(UpdateView):
    model = Usuario
    success_url = reverse_lazy('usuarios')
    fields = ['nombre', 'apellido', 'id_socio', 'email']
    template_name = 'AppEntrega1/sucursales_form.html'
    #Puedo usar el mismo template que SucursalesCreateView
    
class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuarios')
    #Por default usa el template libro_confirm_delete.html

