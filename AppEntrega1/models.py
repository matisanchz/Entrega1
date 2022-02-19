from django.db import models

from django.contrib.auth.models import User

from django.core.validators import RegexValidator

class Sucursal(models.Model):
    
    nombre = models.CharField(max_length=50, verbose_name='Nombre del local')
    localidad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    
    def __str__(self):
        return f'Librería {self.nombre}, ubicada en {self.localidad}'
    
class Seccion(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre de la seccion')
    piso = models.IntegerField()
    
    def __str__(self):
        return f'Sección de {self.nombre}, ubicada en el piso({self.piso})'
    
class Libro(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título completo del libro')
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    editorial = models.CharField(max_length=50)
    disponibilidad = models.BooleanField()
    sitio_oficial = models.URLField()
    
    def __str__(self):
        return f'{self.titulo}, {self.autor}'

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    id_socio = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - Socio nro. {self.id_socio}'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null = True, blank = True)