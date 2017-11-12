from django.shortcuts import render
from core.forms import LoginForm
from core.models import Usuario

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cursos(request):
    return render(request, 'cursos.html')

def detalhe_curso(request):
    return render(request, 'detalhe_curso.html')

def disciplina(request):
    return render(request, 'disciplina.html')

def noticias(request):
    return render(request, 'noticias.html')

def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')

def area_aluno(request):
    return render(request, 'area_aluno.html')

def area_professor(request):
    return render(request, 'area_professor.html')

def primeiro_login(request):
    return render(request, 'primeiro_login.html')

def matricula(request):
    return render(request, 'matricula.html')