from django.shortcuts import render
from .models import Post
# para consultar la base de datos usamos 
from django.shortcuts import get_object_or_404

# Create your views here.

#Creamos la primera vista de la url dentro de este archivo

def render_post(request):
    #Hacer una consulta si no todo esta bien
    posts = Post.objects.all()
    #Renderizar el archivo post.html
    return render (request, 'post.html', {'posts':posts})

# url dinamica || todo depues de 8000/blog/... lo busque como id
# Vista para rederizar los datos buscados

def post_detail(request, post_id):
    #que devuelva 404 si no existe lo que se busca 
    post = get_object_or_404(Post, pk = post_id )
    return render(request, 'post_detail.html', {'post':post})