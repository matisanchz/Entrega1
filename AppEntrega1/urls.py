from django.urls import path

from AppEntrega1.views import SucursalListView, inicio, sucursal, seccion, libro, usuario, empleado

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('sucursales', sucursal, name = 'sucursales'),
    path('secciones', seccion, name = 'secciones'),
    path('libros', libro, name = 'libros'),
    path('usuarios', usuario, name = 'usuarios'),
    path('empleados', empleado, name = 'empleados'),
    
]