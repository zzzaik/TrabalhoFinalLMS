from django import forms
from core.models import ArquivoResposta, ArquivoQuestao

class mensagemForm(forms.Form):
    msg = forms.CharField()

    def msg_limpa(self):
        return self.cleaned_data['msg']

class fileUploadAluno(forms.ModelForm):
    class Meta:
        model = ArquivoResposta
        fields = "__all__"

class fileUploadProf(forms.ModelForm):
    class Meta:
        model = ArquivoQuestao
        fields = "__all__"
