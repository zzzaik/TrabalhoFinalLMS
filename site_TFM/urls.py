"""site_TFM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
<<<<<<< HEAD
from core.views import index, cursos, detalhe_curso, disciplina, noticias, recuperar_senha
=======
from core.views import index, lista_curso, detalhe_curso, disciplina, noticia
from messages.views import mensagem
>>>>>>> origin/master

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^cursos', cursos),
    url(r'^detalhe_curso', detalhe_curso),
    url(r'^disciplina', disciplina),
<<<<<<< HEAD
    url(r'^noticias', noticias),
    url(r'^recuperar_senha', recuperar_senha)
=======
    url(r'^noticia', noticia),
    url(r'^mensagem', mensagem)
>>>>>>> origin/master
]
