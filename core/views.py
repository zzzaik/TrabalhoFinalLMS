from django.shortcuts import render
from core.models import Usuario, CodigoMatricula
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
now = datetime.now()
def checa_aluno(user):
     return user.user_type == 'A'

def checa_professor(user):
     return user.user_type == 'P'

def index(request):
    return render(request, 'index.html')

def cursos(request):
    return render(request, 'cursos.html')

def noticias(request):
    return render(request, 'noticias.html')

def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')

#@login_required(login_url = '/login')
#@user_passes_test(checa_aluno, login_url = '/?erro=acesso', redirect_field_name = None)
def area_aluno(request):
    context = {
        'data_agora': now
    }
    return render(request, 'area_aluno.html', context)

#@login_required(login_url = '/login')
#@user_passes_test(checa_professor, login_url = '/?erro=acesso', redirect_field_name = None)
def area_professor(request):
    context = {
    'data_agora': now
    }
    return render(request, 'area_professor.html', context)

def primeiro_login(request):
    return render(request, 'primeiro_login.html')

def matricula(request):
    return render(request, 'matricula.html')