from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=110)
    content = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=260)
    created_at = models.DateField()

"""
Cuando ya tenemos nuestro modelo o hacemos algun cambio a 
nuestra estructura de tablas requermos hacer migraciones si o si.
Entrando a la ruta del proyecto y ejecutar en consola:
$ Ruta_proyecto>python manage.py makemigrations
Luego ejecutar para sql
$ python manage.py migrate nombre_app nombre_migracion
Luego toca ejecutar y migrar todo esto para que se guarde en la db
$ python manage.py migrate
"""