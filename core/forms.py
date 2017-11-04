from django import forms

class LoginForm(forms.Form):
    ra = forms.CharField(label = 'RA', required = True, max_length = 6, min_length = 6)
    senha = forms.CharField(label = 'Senha', required = True, widget=forms.PasswordInput)
    
    def Logar(self):
        'ra:', self.cleaned_data['ra'],
        'Senha:', self.cleaned_data['senha']