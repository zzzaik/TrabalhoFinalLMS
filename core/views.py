from django.shortcuts import render
from core.forms import LoginForm

# Create your views here.


def index(request):
    log = False
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            form.Logar()
            log = True
    else:
        form = LoginForm()
        log = False
    context = {
        'tipo_user': 'professor',
        'logado': log,
        'formulario_login': form,
    }
    return render(request, 'index.html', context)

def cursos(request):
    context = {
        'tipo_user': 'x'
    }
    return render(request, 'cursos.html', context)

def detalhe_curso(request):
    context = {
        'tipo_user': 'x'
    }
    return render(request, 'detalhe_curso.html', context)

def disciplina(request):
    context = {
        'tipo_user': 'x'
    }
    return render(request, 'disciplina.html', context)

def noticias(request):
    context = {
        'tipo_user': 'x'
    }
    return render(request, 'noticias.html', context)