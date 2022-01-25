from django.urls import path

from AppEntrega1.views import SucursalListView, SucursalCreateView, SucursalDetailView, SucursalUpdateView, SucursalDeleteView, inicio, sucursal, seccion, libro, usuario, empleado, sucursalesFormulario

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('sucursales', SucursalListView.as_view(), name = 'sucursales'),
    # path('sucursalesFormulario', sucursalesFormulario, name = 'sucursalesFormulario'),
    path('sucursales/add', SucursalCreateView.as_view(), name = 'sucursal_add'),
    path('sucursales/view/<pk>', SucursalDetailView.as_view(), name = 'sucursal_view'),
    path('sucursales/update/<pk>', SucursalUpdateView.as_view(), name = 'sucursal_update'),
    path('sucursales/delete/<pk>', SucursalDeleteView.as_view(), name = 'sucursal_delete'),
    path('secciones', seccion, name = 'secciones'),
    path('libros', libro, name = 'libros'),
    path('usuarios', usuario, name = 'usuarios'),
    path('empleados', empleado, name = 'empleados'),
    
]