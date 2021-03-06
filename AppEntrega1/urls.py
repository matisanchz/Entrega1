from django.urls import path

from AppEntrega1.views import home, agregar_avatar, buscar_libro, buscar_sucursal, busqueda_libro, busqueda_sucursal, email_enviado, enviar_email, busqueda_usuario, buscar, pagina_construccion, SucursalListView, SucursalCreateView, SucursalDetailView, SucursalUpdateView, SucursalDeleteView, SeccionListView, SeccionCreateView, SeccionDetailView, SeccionUpdateView, SeccionDeleteView, LibroListView, LibroDetailView, LibroCreateView, LibroUpdateView, LibroDeleteView, UsuarioListView, UsuarioDetailView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView, mi_perfil, editar_perfil

urlpatterns = [
    path('', home, name= 'home'),
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
    path('busquedaLibro', busqueda_libro, name = 'busqueda_libro'),
    path('buscar/libro', buscar_libro, name = 'buscar_libro'),
    path('busquedaSucursal', busqueda_sucursal, name = 'busqueda_sucursal'),
    path('buscar/sucursal', buscar_sucursal, name = 'buscar_sucursal'),
    path('mensajeria', enviar_email, name = 'mensajeria'),
    path('mensajeria/enviado', email_enviado, name = 'enviado'),
    path('user/avatar/add', agregar_avatar, name='avatar_add'),
    path('user/', mi_perfil, name='mi_perfil'),
    path('user/edit', editar_perfil, name='user_editar'),
    path('construccion', pagina_construccion, name='pagina_construccion')
]