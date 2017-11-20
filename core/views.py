from django.shortcuts import render
from core.models import Usuario
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
    ra_alunos=request.POST.getlist('ra_alunos')
    # como passar um array pelo POST; django:
    # https://stackoverflow.com/questions/4581114/django-questionhow-to-pass-a-list-parameter-using-post-method
    context = {
        'cursos':'lista de cursos',#query em função do RA do prof
        'disciplinas':'lista de disciplinas',#disciplinas do curso selecionado
        'turmas':'lista de turmas',#turmas da disciplina selecionada
        'alunos':'lista de alunos',#alunos sem turma
        'matriculas':ra_alunos#vem na forma de um array
    }
    return render(request, 'matricula.html',context)
