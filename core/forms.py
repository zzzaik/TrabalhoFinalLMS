from django import forms


class LoginForm(forms.Form):
    ra = forms.CharField()
    senha = forms.CharField()

    def logar(self):
        retorno = {'ra': self.cleaned_data['ra'], 'senha': self.cleaned_data['senha']}
        return retorno

