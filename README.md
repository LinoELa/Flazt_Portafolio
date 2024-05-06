# Flazt_Portafolio

---- Commit cada 15 - 20 minutos del video ---- 

# -------------  Introduccion ----------------

1. Crear entorno de trabajo 

2. Elegir el interprete de python en VSCode
    -> Video en Flazt

3.  A. Instalar Django con 
        ==> Pip install django

    B. Instalamos Pillow
        ==> 
    C. Crear un espacio de trabajo en VSCode

    D. Crear y conectar Github con VSCode

4. Comenzar un proyecto con
    ==> django-admin startproject django-portafolio . 
            {------- el punto es para que no cree mas carpetas ------- }

5. En caso de poner error de emigraciones () hacer
    ==> python manage.py migrate

## Crear Apps del proyecto
El proyecto tendra 2 apliaciones 
a. Un Front End (Portafolio)
b. Blog


6. Creamos la apliacion con 
    ==> python python manage.py startapp blog
    ==> python python manage.py startapp porfolio

7. Luego hacerle saber a ddjango que hemos creado 2 apliaciones en settings.py y en installed_app registramos la app. 

------ ===== MODELS.PY ======= -----
Son clases de Python que defines que  que puedo guardar dentro de la base de datos.

Editar la inforamcion que se va a mostrar en base de datos 

8. Hacer un migracion con 
    ==> python manage.py makemigrations

9. Ejecutar la migracion : Para crear las tablas 
    ==> python manage.py migrate

10. Hacemmos un 
    ==> python manage.py runserver: 
    se abrira en 

    -> http://127.0.0.1:8000/
    
    -> http://localhost:8000/

# ----------- FIN DE PARTE 1  INTRODUCCION ----------------- 