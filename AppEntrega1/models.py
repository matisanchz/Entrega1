from django.db import models

class Seccion(models.Model):
    
    nombre=models.CharField(max_length=40, verbose_name='Descripcion de la Sección')
    piso = models.IntegerField(verbose_name='Piso de la biblioteca en que está ubicada la sección')
    
    def __str__(self):
        return f'Sección de {self.nombre}, ubicada en el piso ({self.piso})'
    
class Libro(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre completo del libro')
    autor = models.CharField(max_length=50)
    fecha_publicación = models.DateField()
    editorial = models.TextField()
    disponibilidad = models.BooleanField()
    sitio_oficial = models.URLField()
    
    def __str__(self):
        return f'Nombre del libro: {self.nombre}, escrito por {self.autor} el {self.fecha_publicación}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.email})'
