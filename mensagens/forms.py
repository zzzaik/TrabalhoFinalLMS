from django import forms
from core.models import AuthUser
from mensagens.models import Mensagem

class MenssagemForm(forms.Form):
    destinatario=forms.CharField('label = Destinatario',required = True)
    mensagem=forms.CharField('label = Destinatario',required = True)