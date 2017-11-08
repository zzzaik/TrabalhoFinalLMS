from django.shortcuts import render
from mensagens.models import Mensagem
from core.models import AuthUser

# Create your views here.
def mensagem(request):
    if request.POST:
        if request.is_valid():
            user=AuthUser.objects.all()
            context = {
            'remetente':user.username,
    }

