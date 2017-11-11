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
from django.contrib.auth.views import login, logout
from core.views import index, cursos, detalhe_curso, disciplina, noticias, recuperar_senha, area_aluno, area_professor, primeiro_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^cursos', cursos, name='cursos'),
    url(r'^detalhe_curso', detalhe_curso, name='detalhe_curso'),
    url(r'^disciplina', disciplina, name='disciplina'),
    url(r'^noticias', noticias, name='noticias'),
    url(r'^recuperar_senha', recuperar_senha, name='recuperar_senha'),
    url(r'^area_aluno', area_aluno, name='area_aluno'),
    url(r'^area_professor', area_professor, name='area_professor'),
    url(r'^primeiro_login', primeiro_login, name='primeiro_login'),
    url(r'^login', login, {'template_name':'login.html'}),
    url(r'^logout', logout, {'next_page':'/'})
]
