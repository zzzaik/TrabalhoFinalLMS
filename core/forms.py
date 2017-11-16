from django import forms

class mensagemForm(forms.Form):
    msg = forms.CharField()

    def msg_limpa(self):
        return self.cleaned_data['msg']