from django.db import models
# modulo para el texto
from django.db.models.fields import CharField, URLField
# modulo para el manejo de las imagenes 
from django.db.models.fields.files import ImageField





# Create your models here.

# guardar informacion en la base de datos 

class Proyect (models.Model):
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    imagen = ImageField(upload_to='portfolio/images/')
    #tengo que poner el model al principio y si quiero el los de arriab tambien
    url= models.URLField(blank=True) 
