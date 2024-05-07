"""
URL configuration for djangoPortafolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#importar include para que pueda leer las carpetas y decidir que sera importado
from django.urls import include


# Para las imagenes 
from django.conf.urls.static import static
from django.conf import settings

# Para las vistas 
from portfolio import views

#traer info de post 
from blog import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    #al visitar la pagina blog que traiga lo que hay alli 
    path('blog/', include('blog.urls'))

    
]

    # Para imagenes 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
