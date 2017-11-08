from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request, 'index.html')

def lista_curso(request):
   return render(request, 'lista_curso.html')

def detalhe_curso(request):
   return render(request, 'detalhe_curso.html')

def disciplina(request):
   return render(request, 'disciplina.html')

def noticia(request):
   return render(request, 'noticia.html')

def areaAluno(request):
    return render(request,"areaAluno.html")