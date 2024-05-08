# Flazt_Portafolio

---- Commit cada 15 - 20 minutos del video ---- 
Video Original : 
https://youtu.be/zBjMF6je24U

# -------------  Introduccion ----------------

0. Crear entorno virtual con (en mi caso ANACONDA) :
       ==> conda create -n (nombre) python=(version que tengo)
2. Crear entorno de trabajo 

3. Elegir el interprete de python en VSCode
    -> Video en Flazt

4.  A. Instalar Django con 
        ==> Pip install django

    B. Instalamos Pillow
        ==> 
    C. Crear un espacio de trabajo en VSCode

    D. Crear y conectar Github con VSCode

5. Comenzar un proyecto con
    ==> django-admin startproject django-portafolio . 
            {------- el punto es para que no cree mas carpetas ------- }

6. En caso de poner error de emigraciones () hacer
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




# ----------- PARTE 3  VISTAS :   ----------------- 

1. Crear un archivo urls.py para cada app para dividir las urls dependendiendo de la app
    -->  De hecho primero creamos una urls.py en la App de blog
    Hacemos casi lo mismo pero dirigido a blog 
    a. usamos el post.html para crear la visualizaion en pantalla
    b. Usamos views de blog para la vita 
    c. Usamos urls.py dee blog para configurar el blog 
    d. usamos urls.py de djangoPortafolio para poder unirlo con urls.py de blog importando Include  y usandolo.

2. Creamos el modelo de datos en blog en models.py del blog

    A. luego en la administracion del admin creamos el registro para la publicacion

    B. Registar el nuevo modelo en admin.py de blog

    C. Luego tenemos que hacer la migracion para que la base de datos lo reconozca 
        A: Hacer un migracion con 
            ==> python manage.py makemigrations

        B: Ejecutar la migracion : Para crear las tablas 
            ==> python manage.py migrate

    D. Ir al panel de admistracion y anadir informacion en el post en este caso de blog para probar si todo esta bien y si se ve la imagen.

    E. si "D" esta bien pues hacer una consulta 

3. Hacer una consulta  en el views.py de blog para ver si todo esta  bien 
    A. Configurando la VARIABLE donde de guarfa la informacion y el OBJETO

    B. Para ver si ha estado bien pues en el archivo post.html meterle la Informacion de la base de datos haber si lo muestra
    <h1> Post </h1>

        {% comment %} <pre>{{posts}} </pre> {% endcomment %}
        
        {% for post in posts %}

        <h2> {{post.titulo}}  </h2>
        <h3> {{post.date}}  </h3>
        <p>  {{post.descipcion}} </p>
        <img src = '{{post.imagen.url}}' alt = '{{post.titulo}}'>

        {% endfor %}
4. Como hacer que cada blog tenga una url dinamica en plan
    A. http://127.0.0.1:8000/blog/ el el principal de blog
        ==> http://127.0.0.1:8000/blog/1
        ==> http://127.0.0.1:8000/blog/2
        ==> http://127.0.0.1:8000/blog/3
        ==> http://127.0.0.1:8000/blog/4
        ==> ...
5. Configuar para poner ir al blog que estamso viendo, es como poner unlink abajo


# ----------- PARTE 4 HTML : Layout : Estructura  ----------------- 

Primero entender el concepto de LAYOUT

1. Creamos un un archivo layout.hmtl
    Que sera como el archivo padre del diseno donde todos van a heredar
    ==>{% block content %} 
    ==>{% endblock  %}



2. Luego lo pasamos dentro de los demas archivos.html para que lo puedan heredar 
    ==>{% extends "layout.html" %}

    ==> {% block content  %}
    ==> {% endblock  %}


# ----------- PARTE 4 B BOOTSTRAP  ----------------- 

1. Empezamos vinculando Bootstrap y pegando el link en layout.html
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">


------------------------ Navbar ----------------------------

2. Dentro de la carpeta Template, creamos una carpeta llamada partials y eentro le ponemos un archivo que se llamara navbar.html

    A. se puede crear asi :
        ==> partials/navbar.html


2. Ponemos el navbar de bootstrap que esta en Components

3. Editamos el navbar de bootstrap como queremos que se quede 

    A. Entre las cosas que configuramos son los links del navbar 

     ==> <a class="navbar-brand fw-bold fst-italic" href="/">RR</a>

     ==>   <a class="nav-link" href="{% url 'blog:post' %}">Blog</a>

4. Encuento a descargar quiero que descarge algo
    A. Configuro y estiliso el boton de descargar
    B. Creo una nueva carpeta llamado STATIC : pero es publico
    C. Dentro de la carpeta crear un un archivo el quesea ej: main.css
    D. Luego cargarlo en la pagina que se quiere llamar

            ==> {% load static %}

            Podemos asta ver el codigo del archivo 
            ==> http://127.0.0.1:8000/static/main.css

    E. Dentro de la carpeta static se puede crear otra carpeta (EJ: PORTAFOLIO) donde se le va meter los docomentos (Imagenes, Pdf, Excel , Csv... )

    F. Luego en el boton que se quiere que se descarge se puede pone el link de  la parte mas importante es ' {% static "porfolio/cvPython.pdf"%}' 
        ==> <a class="btn btn-primary btn-sm" href="{% static "porfolio/cvPython.pdf"%}" target='_blank' >Descargar CV</a>
        
------------------------ Seccion 1  ----------------------------

Ahora vamos a estilizar la seccion 1 

Es los ultimos 20 minutos donde estiliza la pagina



# ----------- PARTE 5 : FINAL ----------------- 

VAMOS A PREPARAR EL PROYECTO PARA EL DESPLIQUE Y DECIR CUALES ARCCHIVOS SON MAS IMPORTANTE

1. Con PIP para generar las dependencias relacionados a este proyecto : Que lo guarde en requierements
    ==> pip freeze > requirements.txt

2. Crear GITIGNORE para que ignore los archivos que no son necesarios 
    Dentro le ponemos las carpetas y archivos que tiene que ignorar 








# --------------------- FIN ----------------- 
