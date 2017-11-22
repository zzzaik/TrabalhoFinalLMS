from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from core.forms import mensagemForm
from core.models import Usuario, Aluno, Curso


def checa_aluno(user):
    return user.user_type == 'A'


def checa_professor(user):
    return user.user_type == 'P'


def index(request):
    return render(request, 'index.html')


def cursos(request):
    curso = Curso.objects.all()
    context = {
        "cursos":curso,
    }
    return render(request, "cursos.html", context)


def noticias(request):
    return render(request, 'noticias.html')


def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')


@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?erro=acesso', redirect_field_name=None)
def area_aluno(request):
    return render(request, 'area_aluno.html')


@login_required(login_url='/entrar')
@user_passes_test(checa_professor, login_url='/?erro=acesso', redirect_field_name=None)
def area_professor(request):
    return render(request, 'area_professor.html')


def primeiro_login(request):
    return render(request, 'primeiro_login.html')


def matricula(request):
    return render(request, 'matricula.html')

def pag_curso(request, sigla):
    curso = Curso.objects.get(sigla=sigla.upper())
    contexto = {
        "cursos":curso,
    }
    return render(request,"pag_curso.html",contexto)
