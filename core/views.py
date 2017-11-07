from django.shortcuts import render
from core.forms import LoginForm
from criar_aluno.models import Aluno
from core.models import AuthUser

# Create your views here.
def index(request):
    sessao = False
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.logar()
            ''' Código view login ainda incompleto
            user = AuthUser.objects.all()
            for username in user:
                for quebra in username:
                    if quebra == ',':
                        username.index()

                print(dados_user)
                if user == login['ra']:
                    pass
                else:
                    pass
            sessao == True
            prim_login = user['first_login']
            tipo_user = user['user_type']
            '''
            sessao = True
            prim_login = True
            tipo_user = 'Professor'
    else:
        form = LoginForm()
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
            login = form.logar()
            ''' Código view login ainda incompleto
            user = AuthUser.objects.all()
            for username in user:
                for quebra in username:
                    if quebra == ',':
                        username.index()

                print(dados_user)
                if user == login['ra']:
                    pass
                else:
                    pass
            sessao == True
            prim_login = user['first_login']
            tipo_user = user['user_type']
            '''
            sessao = True
            prim_login = True
            tipo_user = 'Professor'
    else:
        form = LoginForm()
        sessao = False
        prim_login = False
        tipo_user = False
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
            login = form.logar()
            ''' Código view login ainda incompleto
            user = AuthUser.objects.all()
            for username in user:
                for quebra in username:
                    if quebra == ',':
                        username.index()

                print(dados_user)
                if user == login['ra']:
                    pass
                else:
                    pass
            sessao == True
            prim_login = user['first_login']
            tipo_user = user['user_type']
            '''
            sessao = True
            prim_login = True
            tipo_user = 'Professor'
    else:
        form = LoginForm()
        sessao = False
        prim_login = False
        tipo_user = False
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
            login = form.logar()
            ''' Código view login ainda incompleto
            user = AuthUser.objects.all()
            for username in user:
                for quebra in username:
                    if quebra == ',':
                        username.index()

                print(dados_user)
                if user == login['ra']:
                    pass
                else:
                    pass
            sessao == True
            prim_login = user['first_login']
            tipo_user = user['user_type']
            '''
            sessao = True
            prim_login = True
            tipo_user = 'Professor'
    else:
        form = LoginForm()
        sessao = False
        prim_login = False
        tipo_user = False
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
            login = form.logar()
            ''' Código view login ainda incompleto
            user = AuthUser.objects.all()
            for username in user:
                for quebra in username:
                    if quebra == ',':
                        username.index()

                print(dados_user)
                if user == login['ra']:
                    pass
                else:
                    pass
            sessao == True
            prim_login = user['first_login']
            tipo_user = user['user_type']
            '''
            sessao = True
            prim_login = True
            tipo_user = 'Professor'
    else:
        form = LoginForm()
        sessao = False
        prim_login = False
        tipo_user = False
    context = {
        'tipo_user': tipo_user,
        'logado': sessao,
        'formulario_login': form,
        'prim_login': prim_login
    }
    return render(request, 'noticias.html', context)

def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')
