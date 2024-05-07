from django.db import models

#para el uso de datetime , fecha y hora
import datetime

# Create your models here.


# voy a usar una nueva forma sin necesidad de importar los modulos
# Definimos el modelo
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descipcion = models.TextField()
    # Que cree una nueva carpeta llamada blog y dentro  otra images
    # Dentro de images entaran las imagenes  
    imagen = models.ImageField( upload_to='blog/images')
    # si no se pone pues que ponga la fecha actual 
    date = models.DateField(datetime.date.today)

