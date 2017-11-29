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
        "cursos": curso,
    }
    return render(request, "cursos.html", context)


def noticias(request):
    return render(request, 'noticias.html')


@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?erro=acesso', redirect_field_name=None)
def area_aluno(request):
    context = {
        'data_agora': now
    }
    return render(request, 'area_aluno.html', context)


@login_required(login_url='/entrar')
@user_passes_test(checa_professor, login_url='/?erro=acesso', redirect_field_name=None)
def area_professor(request):
    return render(request, 'area_professor.html')


@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?erro=acesso', redirect_field_name=None)
def matricula(request):
    time = now
    aluno = Aluno.objects.get(ra=request.user.ra)
    cursos = []
    turmas = []
    disciplinas = []
    curso_turma = []
    cont_post = ['csrfmiddlewaretoken', 'ano', 'semestre', 'turma']
    disciplina_ofertada = DisciplinaOfertada.objects.filter(
        ano=aluno.ano_ingresso, semestre=aluno.semestre)
    for x in range(0, len(disciplina_ofertada)):
        curso_turma = CursoTurma.objects.filter(
            sigla_curso=aluno.curso_id, ano_ofertado=disciplina_ofertada[x].id, semestre_ofertado=disciplina_ofertada[x].id)
        for y in curso_turma:
            disciplinas.append(y.nome_disciplina)
            if str(y.id_turma) not in turmas:
                turmas.append(str(y.id_turma))
    if request.POST:
        post_turma = (request.POST.get("turma"))
        if (post_turma != "-- Turma --"):
            pass
        else:
            for y in request.POST.keys():
                if y not in cont_post:
                    cont_post.append(y)
            for x in range(4, len(cont_post)):
                if request.POST[cont_post[x]]:
                    d = Disciplina.objects.get(id=request.POST[cont_post[x]])
                    do = DisciplinaOfertada.objects.get(nome_disciplina=d)
                    t = Turma.objects.get(nome_disciplina=d)
                    if Matricula.objects.get(ra_aluno=aluno, nome_disciplina=d, ano_ofertado=do, semestre_ofertado=do, id_turma=t):
                        pass
                    else:
                        Matricula.objects.create(
                            ra_aluno=aluno, nome_disciplina=d, ano_ofertado=do, semestre_ofertado=do, id_turma=t)
                else:
                    pass
            curso_turma = ''
            disciplinas = ''
    else:
        curso_turma = ''
        disciplinas = ''
    contexto = {
        "curso_turma": curso_turma,
        "turmas": turmas,
        "disciplinas": disciplinas,
        "mes_atual": time.month,
        "ano_atual": time.year
    }

    return render(request, 'matricula.html', contexto)


@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?erro=acesso', redirect_field_name=None)
def historico(request):
    disciplinas = request.POST.getlist('disciplinas')
    # como passar um array pelo POST; django:
    # https://stackoverflow.com/questions/4581114/django-questionhow-to-pass-a-list-parameter-using-post-method
    context = {
        'cursos': 'lista de cursos',  # query em função do RA do aluno
        'disciplinas': disciplinas,  # disciplinas selecionadas p/ matrícula
        'turmas': 'lista de turmas',  # turmas da disciplina selecionada
        'matricula': 'ra_aluno'  # pego na sessão
    }
    return render(request, 'historico.html', context)


def pag_curso(request, sigla):
    curso = Curso.objects.get(sigla_curso=sigla.upper())
    contexto = {
        "cursos": curso,
    }
    return render(request, "pag_curso.html", contexto)


@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?erro=acesso', redirect_field_name=None)
def msg_aluno(request):
    context = {
        'user': ['aluno 1', 'aluno 2', 'aluno 3', 'aluno 4'],
        'mensagem': 'texto\ntexto\ntexto',
        'data_agora': now
    }
    return render(request, 'msg_aluno.html', context)


@login_required(login_url='/entrar')
@user_passes_test(checa_professor, login_url='/?erro=acesso', redirect_field_name=None)
def msg_professor(request):
    context = {
        'cursos': ['ADS', 'BD'],
        'turmas': ['2A', '2B'],
        'alunos': {
            'aluno1': ['ADS', '2A'],
            'aluno2': ['ADS', '2B'],
            'aluno3': ['BD', '2A'],
            'aluno4': ['BD', '2B'],
        },
        'mensagem': 'texto\ntexto\ntexto',
        'data_agora': now

    }
    return render(request, 'msg_professor.html', context)


@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?erro=acesso', redirect_field_name=None)
def upload_aluno(request):
    aluno = Aluno.objects.get(ra=request.user.ra)
    disciplinas = []
    turmas = []
    ano = []
    semestre = []
    disciplina_ofertada = DisciplinaOfertada.objects.filter(ano=aluno.ano_ingresso, semestre=aluno.semestre)
    for x in range(0, len(disciplina_ofertada)):
        curso_turma = CursoTurma.objects.filter(
            sigla_curso=aluno.curso_id, ano_ofertado=disciplina_ofertada[x].id, semestre_ofertado=disciplina_ofertada[x].id)
        for y in curso_turma:
            disciplinas.append(y.nome_disciplina)
            ano.append(y.ano_ofertado)
            semestre.append(y.semestre_ofertado)
            if str(y.id_turma) not in turmas:
                turmas.append(str(y.id_turma))
    if request.POST:
        form = fileUploadAluno(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.ra_aluno = aluno.ra
            #d = Disciplina.objects.get(id=request.POST[cont_post[x]])
            #do = DisciplinaOfertada.objects.get(nome_disciplina=d)
            #t = Turma.objects.get(nome_disciplina=d)
            #ArquivoResposta.objects.create()
    else:
        form = fileUploadAluno()

    contexto = {
        "form": form,
        "disciplinas": disciplinas,
        'turmas': turmas,
        'ano': ano,
        'semestre': semestre
    }
    return render(request, 'upload_aluno.html', contexto)


@login_required(login_url='/entrar')
@user_passes_test(checa_professor, login_url='/?erro=acesso', redirect_field_name=None)
def upload_prof(request):
    prof = Professor.objects.get(ra=request.user.ra)
    turmas = []
    for t in Turma.objects.filter(ra_professor=prof):
        turmas.append(t)
    if request.POST:
        arquivo = ArquivoQuestao()
        form = fileUploadProf(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = fileUploadProf()

    contexto = {
        "form": form,
        "turmas": turmas

    }
    return render(request, 'upload_prof.html', contexto)


@login_required(login_url='/entrar')
@user_passes_test(checa_aluno, login_url='/?erro=acesso', redirect_field_name=None)
def exibir_boletim(request):
    #notas = []
    #contador = 0
    #aluno = Aluno.objects.get(parent_link=request.user.id)
    #matriculas = Matricula.objects.filter(ra_aluno=aluno) 
    #boletim = {}

    #for disciplinas in matriculas.Matricula.nome_disciplina:
    #    boletim = {disciplinas.nome_diciplina}
    #    for notas in Resposta.objects.filter(ra_aluno=aluno, nome_disciplina=disciplinas.nome_disciplina):
    #        contador += 1
    #        notas.append(nota.nota)

    #    media = notas / contador
    #    boletim[disciplinas.nome_diciplina] = media
    #    contador = 0

    #--STUB--
    boletim = {
        'semestre_ofertado':'2º Semestre',
        'disciplinas':{
            'Linguagem de Programação II':'8.5',
            'Linguagem SQL':'9.0',
            'Gestão de Projetos':'8.0',
            'Engenharia de Software':'7.7',
            'Tecnologia Web':'10.0'
        }
    }
    contexto = {
        "boletim": boletim
    }
    return render(request, 'boletim.html', contexto)
