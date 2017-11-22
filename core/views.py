from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from core.forms import mensagemForm
from core.models import Usuario, CodigoMatricula, Aluno
from core.codes import gera_senha


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


@login_required(login_url='/login')
@user_passes_test(checa_aluno, login_url='/?erro=acesso', redirect_field_name=None)
def area_aluno(request):
    return render(request, 'area_aluno.html')


@login_required(login_url='/login')
@user_passes_test(checa_professor, login_url='/?erro=acesso', redirect_field_name=None)
def area_professor(request):
    return render(request, 'area_professor.html')

@login_required(login_url='/login')
@user_passes_test(checa_professor, login_url='/?erro=acesso', redirect_field_name=None)
def gerar_codigo(request):
    if request.POST:
        user = Usuario.objects.filter(user_type='A')
        for aluno in request.POST.keys():
            if aluno != 'csrfmiddlewaretoken':
                x = Aluno.objects.get(ra=int(aluno))
                if x.id not in CodigoMatricula.objects.all():
                    codigo = CodigoMatricula.objects.create(
                        id_aluno=Aluno.objects.get(ra=int(aluno)), codigo=gera_senha(10), stat='1')
    else:
        user = Usuario.objects.filter(user_type='A')
    context = {
        'alunos': user
    }
    return render(request, 'gerar_codigo.html', context)


def primeiro_login(request):
    return render(request, 'primeiro_login.html')


def matricula(request):
    return render(request, 'matricula.html')
