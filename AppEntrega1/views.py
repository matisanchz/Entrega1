from django.forms import model_to_dict

from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Sucursal, Seccion, Libro, Usuario, Empleado

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

def inicio(request):
    return render(request, 'AppEntrega1/inicio.html')

def sucursal(request):
    return render(request, 'AppEntrega1/sucursal.html', {'sucursales': Sucursal.objects.all()})

def sucursalesFormulario(request):
    return render(request, 'AppEntrega1/sucursalesFormulario.html')

def seccion(request):
    return HttpResponse('seccion')

def libro(request):
    return HttpResponse('libro')

def empleado(request):
    return HttpResponse('empleado')

def usuario(request):
    return HttpResponse('usuario')
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
