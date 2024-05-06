from django.shortcuts import render
#Para traer la informacion de los archivos 

from .models import Proyect






# Create your views here.

def home(request):
    projects = Proyect.objects.all()
            # {'projects':projects} ==> Para traer y mostras los proyectos
    return render(request , 'home.html', {'projects':projects} ) 
