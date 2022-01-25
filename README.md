# Entrega1
Entrega intermedia Proyecto Final

Matías Sánchez Abrego:
Se dió de alta el repositorio de la nube, y se lo instaló en el repositorio local, con git clone.
Se creó el proyecto con django-admin startproject Entrega1.
Se creó la app con python manage.py startapp AppEntrega1.
Se provó el correcto funcionamiento de la app con python manage.py runserver.

Matías Martos:
Creó los modelos, desde models.py, e importó la base de datos con python manage.py makemigrations; y python manage.py migrate.

Matías Sánchez Abrego:
Importó la carpeta static, usando de ejemplo lo visto en la clase.
Se importó la carpeta padre.html, usada en clase.
Creamos el archivo views.py, usando clases para crear formularios en cada modelo. 
Separamos las URLS del proyecto, de las URLS de la AppEntrega1.
Se fue probando uno por uno los formularios, desde runserver, creando los templates correspondientes, e importando las URLS.
Se dio de alta un superusuario en admin:
    Usuario: Biblioteca
    Pass: Entrega1
Se incorporó en el archivo admin.py, los modelos correspondientes, y se verificó el correcto funcionamiento de la Base de datos, viendo desde el panel /admin.
Se incorporó un botón desde padre.html para poder buscar, usando un formulario, el ID de Usuarios creados.
Incorporé paneles de ayuda y contacto. Se modificaron algunos templates, y se debugeo el código.


