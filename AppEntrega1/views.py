from django.forms import model_to_dict

from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Seccion, Libro, Cliente

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

def inicio(request):
    return render(request, 'AppEntrega1/inicio.html')

def seccion(request):
    return render(request, 'AppEntrega1/seccion.html', {'seccion': Seccion.objects.all()})

def libro(request):
    return HttpResponse('libro')

def cliente(request):
    return HttpResponse('cliente')
class SeccionListView(ListView):
    model = Seccion
    template_name = 'AppEntrega1/seccion.html'
    context_object_name = 'seccion'
class SeccionCreateView(CreateView):
    model = Seccion
    success_url = reverse_lazy('seccion')
    fields = ['nombre', 'piso']
    # template_name = 'AppEntrega1/profesor_form.html'
