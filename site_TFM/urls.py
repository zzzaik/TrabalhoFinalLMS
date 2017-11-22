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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from core.views import index, cursos, noticias, recuperar_senha, area_aluno, area_professor, primeiro_login, matricula, pag_curso

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='coordenador'),
    url(r'^$', index, name='home'),
    url(r'^cursos', cursos, name='cursos'),
    url(r'^cursos/(?P<sigla>[A-Z,a-z]+)', pag_curso, name='pag_curso'),
    url(r'^noticias', noticias, name='noticias'),
    url(r'^aluno', area_aluno, name='aluno'),
    url(r'^professor', area_professor, name='professor'),
    url(r'^primeiro_login', primeiro_login, name='primeiro_login'),
    url(r'^entrar', login, {'template_name':'login.html'}, name='entrar'),
    url(r'^entrar/recuperar_senha', recuperar_senha, name='recuperar_senha'),
    url(r'^sair', logout, {'next_page':'/'}, name='sair'),
    url(r'^matricula', matricula, name='matricula'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
