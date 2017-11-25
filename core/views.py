from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from core.forms import mensagemForm, fileUploadAluno, fileUploadProf
from core.models import *

now = datetime.now()
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
    context = {
        'data_agora': now
    }
    return render(request, 'area_aluno.html',context)


@login_required(login_url='/entrar')
@user_passes_test(checa_professor, login_url='/?erro=acesso', redirect_field_name=None)
def area_professor(request):
    return render(request, 'area_professor.html')


def primeiro_login(request):
    return render(request, 'primeiro_login.html')


def matricula(request):
    disciplinas=request.POST.getlist('disciplinas')
    # como passar um array pelo POST; django:
    # https://stackoverflow.com/questions/4581114/django-questionhow-to-pass-a-list-parameter-using-post-method
    context = {
        'cursos':'lista de cursos',#query em função do RA do aluno
        'disciplinas':disciplinas,#disciplinas selecionadas p/ matrícula
        'turmas':'lista de turmas',#turmas da disciplina selecionada
        'matricula':'ra_aluno'#pego na sessão
    }
    return render(request, 'matricula.html',context)

def historico(request):
    disciplinas=request.POST.getlist('disciplinas')
    # como passar um array pelo POST; django:
    # https://stackoverflow.com/questions/4581114/django-questionhow-to-pass-a-list-parameter-using-post-method
    context = {
        'cursos':'lista de cursos',#query em função do RA do aluno
        'disciplinas':disciplinas,#disciplinas selecionadas p/ matrícula
        'turmas':'lista de turmas',#turmas da disciplina selecionada
        'matricula':'ra_aluno'#pego na sessão
    }
    return render(request, 'historico.html',context)

def pag_curso(request, sigla):
    curso = Curso.objects.get(sigla_curso=sigla.upper())
    contexto = {
        "cursos":curso,
    }
    return render(request,"pag_curso.html",contexto)

def msg_aluno(request):
    context = {
        'user':['aluno 1','aluno 2','aluno 3','aluno 4'],
        'mensagem':'texto\ntexto\ntexto',
        'data_agora':now
    }
    return render(request, 'msg_aluno.html',context)

def msg_professor(request):
    context = {
        'cursos':['ADS','BD'],
        'turmas':['2A','2B'],
        'alunos':{
            'aluno1':['ADS','2A'],
            'aluno2':['ADS','2B'],
            'aluno3':['BD','2A'],
            'aluno4':['BD','2B'],
            },
        'mensagem':'texto\ntexto\ntexto',
        'data_agora':now

    }
    return render(request, 'msg_professor.html',context)

def upload_aluno(request):
    aluno = Aluno.objects.get(ra=request.user.ra)
    matriculas = []
    for m in Matricula.objects.filter(ra_aluno=aluno):
        matriculas.append(m)
    
    if request.POST:
        arquivo = ArquivoResposta(ra_aluno=aluno)
        form = fileUploadAluno(request.POST,request.FILES,instance=aluno)
        if form.is_valid():
            form.ra_aluno=aluno.ra
            form.save()
    else:
        
        form = fileUploadAluno()

    contexto = {
        "form":form,
        "matriculas":matriculas,
    }
    return render(request,'upload_aluno.html',contexto)

def upload_prof(request):
    prof = Professor.objects.get(ra=request.user.ra)
    turmas = []
    for t in Turma.objects.filter(ra_professor=prof):
        turmas.append(t)
    
    if request.POST:
        arquivo = ArquivoQuestao()
        form = fileUploadProf(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = fileUploadProf()

    contexto = {
        "form":form,
        "turmas":turmas
        
    }
    return render(request,'upload_prof.html',contexto)