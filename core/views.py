from django.shortcuts import render
from core.forms import LoginForm
from core.models import Usuario
#from djangp.contrib.auth.

# Create your views here.
def index(request):
    sessao = False
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.logar()
            #test_login = AuthUser.objects.all()
            #for usuario in test_login:
            #    if str(usuario) == login['ra']:
            #        user = AuthUser.objects.get(username = login['ra'])
            #        sessao = True
            #        prim_login = user.first_login
            #        tipo_user = user.user_type
            #        ''' Verificação de senha
            #        if user.password == login['senha']:
            #            sessao == True
            #            prim_login = user.first_login
            #            tipo_user = user.user_type
            #        else:
            #            sessao = False
            #            prim_login = False
            #            tipo_user = False
            #    else:
            #        if sessao == False:
            sessao = False
            prim_login = False
            tipo_user = False
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
            #test_login = AuthUser.objects.all()
            #for usuario in test_login:
            #    if str(usuario) == login['ra']:
            #        user = AuthUser.objects.get(username = login['ra'])
            #        sessao = True
            #        prim_login = user.first_login
            #        tipo_user = user.user_type
            #        ''' Verificação de senha
            #        if user.password == login['senha']:
            #            sessao == True
            #            prim_login = user.first_login
            #            tipo_user = user.user_type
            #        else:
            #            sessao = False
            #            prim_login = False
            #            tipo_user = False
            #    else:
            #        if sessao == False:
            sessao = False
            prim_login = False
            tipo_user = False
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
            #test_login = AuthUser.objects.all()
            #for usuario in test_login:
            #    if str(usuario) == login['ra']:
            #        user = AuthUser.objects.get(username = login['ra'])
            #        sessao = True
            #        prim_login = user.first_login
            #        tipo_user = user.user_type
            #        ''' Verificação de senha
            #        if user.password == login['senha']:
            #            sessao == True
            #            prim_login = user.first_login
            #            tipo_user = user.user_type
            #        else:
            #            sessao = False
            #            prim_login = False
            #            tipo_user = False
            #    else:
            #        if sessao == False:
            sessao = False
            prim_login = False
            tipo_user = False
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
            #test_login = AuthUser.objects.all()
            #for usuario in test_login:
            #    if str(usuario) == login['ra']:
            #        user = AuthUser.objects.get(username = login['ra'])
            #        sessao = True
            #        prim_login = user.first_login
            #        tipo_user = user.user_type
            #        ''' Verificação de senha
            #        if user.password == login['senha']:
            #            sessao == True
            #            prim_login = user.first_login
            #            tipo_user = user.user_type
            #        else:
            #            sessao = False
            #            prim_login = False
            #            tipo_user = False
            #    else:
            #        if sessao == False:
            sessao = False
            prim_login = False
            tipo_user = False
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
            #test_login = AuthUser.objects.all()
            #for usuario in test_login:
            #    if str(usuario) == login['ra']:
            #        user = AuthUser.objects.get(username = login['ra'])
            #        sessao = True
            #        prim_login = user.first_login
            #        tipo_user = user.user_type
            #        ''' Verificação de senha
            #        if user.password == login['senha']:
            #            sessao == True
            #            prim_login = user.first_login
            #            tipo_user = user.user_type
            #        else:
            #            sessao = False
            #            prim_login = False
            #            tipo_user = False
            #    else:
            #        if sessao == False:
            sessao = False
            prim_login = False
            tipo_user = False
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

def area_aluno(request):
    return render(request, 'area_aluno.html')

def area_professor(request):
    return render(request, 'area_professor.html')

def primeiro_login(request):
    return render(request, 'primeiro_login.html')