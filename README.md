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

# ----------- PARTE 2  ADMIN : VISTAS  ----------------- 


1. Configurar admin 
    Creamos un usuario con 
    ==>  python manage.py createsuperuser
    - Nombre : ela
    - Password : 123456789

    admin.py --> 
    desde alli podemos confugurar nuestro panel admin


    Al añadir las imagenes en el proyecto por admin se crea una carpeta automatica  con el nombre de : Imagenes

2. Configurar la seccion para poner las fotos en settings.py

    MEDIA_ROOT = BASE_DIR / "media" ->[Para new la carpeta {MEDIA}]

3. Crear vistas .html para el Front End

    Debemos crear primero la carpeta TEMPLATE dentro 
    Dentro de la carpeta template crear los archivos index.html

    Las vistas se configuran desde el el archivo de views.py de dentro de la App que se quiere cambiar en este caso Portfolio
    Creamos una funcion dentro para hacer el render.

    Luego ponemos la nueva ruta en  urls.py de la carpeta principal.

4. Hacer que se muestre de los proyecto creados 
    -> Hacer traer en la pantalla la informacion de los proyectos que tenemos en la base de datos 

    ->tenemos que hacer una consulta a la base de datos
    Primero tramaemos el modelo de datos a al archivo views.py de la carpeta portafolio




