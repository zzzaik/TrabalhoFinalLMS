from django import forms


class LoginForm(forms.Form):
    ra = forms.CharField()
    senha = forms.CharField()

    def logar(self):
        retorno = {'ra': self.cleaned_data['ra'], 'senha': self.cleaned_data['senha']}
        return retorno

class MatriculaForm(forms.Form):
    nomeCompleto = forms.CharField()
    celular = forms.CharField()
    email = forms.Charfield()

    def matricular(self):
        retorno = {'nomeCompleto': self.cleaned_data['nomeCompleto'], 'celular': self.cleaned_data['celular'], 'email':self.cleaned_data['email']}
        return retorno
