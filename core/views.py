from django.shortcuts import render
from core.forms import LoginForm
from criar_aluno.models import Aluno
from core.models import AuthUser

# Create your views here.
def index(request):
    sessao = False
    if request.POST:
        form = LoginForm(request.POST['ra'], request.POST['senha'])
        login = form.logar()
        user = AuthUser.objects.filter('username' == login[1])
        if login[0] == 0:
            sessao = False
            prim_login = False
            tipo_user = False
        elif login[0] == 1:
            sessao == True
            prim_login = user['first_login']
            tipo_user = user['user_type']
    else:
        form = LoginForm('000000', '000000')
        sessao = False
        prim_login = False
        tipo_user = False
    context = {
        'tipo_user': tipo_user,
        'logado': sessao,
        'formulario_login': form,
        'prim_login': prim_login
    }
    return render(request, 'index.html', context)

def cursos(request):
    sessao = False
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.Logar()
            user = AuthUser.objects.filter('username' == login[1])
            if login[0] == 0:
                sessao = False
                prim_login = False
                tipo_user = False
            elif login[0] == 1:
                sessao == True
                prim_login = user['first_login']
                tipo_user = user['user_type']
    else:
        form = LoginForm()
        sessao = False
    context = {
        'tipo_user': tipo_user,
        'logado': sessao,
        'formulario_login': form,
        'prim_login': prim_login
    }
    return render(request, 'cursos.html', context)

def detalhe_curso(request):
    sessao = False
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.Logar()
            user = AuthUser.objects.filter('username' == login[1])
            if login[0] == 0:
                sessao = False
                prim_login = False
                tipo_user = False
            elif login[0] == 1:
                sessao == True
                prim_login = user['first_login']
                tipo_user = user['user_type']
    else:
        form = LoginForm()
        sessao = False
    context = {
        'tipo_user': tipo_user,
        'logado': sessao,
        'formulario_login': form,
        'prim_login': prim_login
    }
    return render(request, 'detalhe_curso.html', context)

def disciplina(request):
    sessao = False
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.Logar()
            user = AuthUser.objects.filter('username' == login[1])
            if login[0] == 0:
                sessao = False
                prim_login = False
                tipo_user = False
            elif login[0] == 1:
                sessao == True
                prim_login = user['first_login']
                tipo_user = user['user_type']
    else:
        form = LoginForm()
        sessao = False
    context = {
        'tipo_user': tipo_user,
        'logado': sessao,
        'formulario_login': form,
        'prim_login': prim_login
    }
    return render(request, 'disciplina.html', context)

def noticias(request):
    sessao = False
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.Logar()
            user = AuthUser.objects.filter('username' == login[1])
            if login[0] == 0:
                sessao = False
                prim_login = False
                tipo_user = False
            elif login[0] == 1:
                sessao == True
                prim_login = user['first_login']
                tipo_user = user['user_type']
    else:
        form = LoginForm()
        sessao = False
    context = {
        'tipo_user': tipo_user,
        'logado': sessao,
        'formulario_login': form,
        'prim_login': prim_login
    }
    return render(request, 'noticias.html', context)

def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')