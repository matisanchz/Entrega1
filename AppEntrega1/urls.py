from django.urls import path

from AppEntrega1.views import inicio, busqueda_usuario, buscar, ayuda, contacto, SucursalListView, SucursalCreateView, SucursalDetailView, SucursalUpdateView, SucursalDeleteView, SeccionListView, SeccionCreateView, SeccionDetailView, SeccionUpdateView, SeccionDeleteView, LibroListView, LibroDetailView, LibroCreateView, LibroUpdateView, LibroDeleteView, UsuarioListView, UsuarioDetailView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('sucursales', SucursalListView.as_view(), name = 'sucursales'),
    path('sucursales/add', SucursalCreateView.as_view(), name = 'sucursal_add'),
    path('sucursales/view/<pk>', SucursalDetailView.as_view(), name = 'sucursal_view'),
    path('sucursales/update/<pk>', SucursalUpdateView.as_view(), name = 'sucursal_update'),
    path('sucursales/delete/<pk>', SucursalDeleteView.as_view(), name = 'sucursal_delete'),
    path('secciones', SeccionListView.as_view(), name = 'secciones'),
    path('secciones/add', SeccionCreateView.as_view(), name = 'seccion_add'),
    path('secciones/view/<pk>', SeccionDetailView.as_view(), name = 'seccion_view'),
    path('secciones/update/<pk>', SeccionUpdateView.as_view(), name = 'seccion_update'),
    path('seccion/delete/<pk>', SeccionDeleteView.as_view(), name = 'seccion_delete'),
    path('libros', LibroListView.as_view(), name = 'libros'),
    path('libros/add', LibroCreateView.as_view(), name = 'libro_add'),
    path('libros/view/<pk>', LibroDetailView.as_view(), name = 'libro_view'),
    path('libros/update/<pk>', LibroUpdateView.as_view(), name = 'libro_update'),
    path('libros/delete/<pk>', LibroDeleteView.as_view(), name = 'libro_delete'),
    path('usuarios', UsuarioListView.as_view(), name = 'usuarios'),
    path('usuarios/add', UsuarioCreateView.as_view(), name = 'usuario_add'),
    path('usuarios/view/<pk>', UsuarioDetailView.as_view(), name = 'usuario_view'),
    path('usuarios/update/<pk>', UsuarioUpdateView.as_view(), name = 'usuario_update'),
    path('usuarios/delete/<pk>', UsuarioDeleteView.as_view(), name = 'usuario_delete'),
    path('busquedaUsuario', busqueda_usuario, name = 'busqueda_usuario'),
    path('buscar', buscar, name = 'buscar'),
    path('ayuda', ayuda, name = 'ayuda'),
    path('contacto', contacto, name = 'contacto'),
]