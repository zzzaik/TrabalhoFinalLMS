from django import forms
from core.models import AuthUser
from criar_aluno.models import Aluno

class LoginForm(forms.Form):
    ra = forms.CharField(label = 'ra', required = True)
    senha = forms.CharField(label = 'senha', required = True, widget=forms.PasswordInput)

    def __init__(self, ra, senha):
        self.ra = ra
        self.senha = senha

    def logar(self):
        user = AuthUser.objects.filter('username' == str(self.ra))
        user_ra = user['username']
        user_passrd = user['password']
        retorno = []
        if self.cleaned_data['ra'] == user_ra and self.cleaned_data['senha'] == user_passrd:
            retorno.append(1)
            retorno.append(str(self.ra))
            return retorno
        else:
            retorno.append(0)
            retorno.append('NULL')
            return retorno
        
        def __str__(self):
            return self.ra
