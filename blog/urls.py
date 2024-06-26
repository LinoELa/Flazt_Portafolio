
#Nosotros hemos creado esta url para poder dividir las urls del proyecto en  cada App

#importamos el path
from django.urls import path
# importamos la funcion de el archivo views
from .views import render_post, post_detail



#para navegar a una de la publiaciones 
app_name = 'blog' #para referenciar a los post de urlpatterns

urlpatterns = [
    path('', render_post, name='post'),
    # url dinamica || todo depues de 8000/blog/... lo busque como id
    path('<int:post_id>', post_detail, name= 'post_detail')
]
