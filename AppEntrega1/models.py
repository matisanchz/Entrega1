from django.db import models

class Sucursal(models.Model):
    
    nombre = models.CharField(max_length=50, verbose_name='Nombre del local')
    localidad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    
    def __str__(self):
        return f'Sucursal {self.nombre}, ubicada en ({self.localidad})'
    
class Seccion(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre de la seccion')
    piso = models.IntegerField()
    
    def __str__(self):
        return f'Sección de {self.nombre}, ubicada en el piso({self.piso})'
    
class Libro(models.Model):
    titulo = models.CharField(max_length=30, verbose_name='Título completo del libro')
    autor = models.CharField(max_length=50)
    fecha_publicación = models.DateField()
    editorial = models.TextField()
    disponibilidad = models.BooleanField()
    sitio_oficial = models.URLField()
    
    def __str__(self):
        return f'Nombre del libro: {self.titulo}, escrito por {self.autor} el {self.fecha_publicación}'

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    id_socio = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.email}) - Socio {self.id_socio}'

class Empleado(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - Empleado a cargo de ({self.cargo})'