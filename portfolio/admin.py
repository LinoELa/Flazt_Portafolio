from django.contrib import admin

# Importar la funcion Project de models en Porfolio
from .models import Proyect



# Register your models here.

#Registrando el primer proyecto
admin.site.register(Proyect)
