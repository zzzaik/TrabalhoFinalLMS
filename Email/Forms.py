from django import forms

class FormularioContato(forms.Form):
    correio = forms.EmailField()
    mensagem = forms.CharField()

class Formulario(forms.form):
    nome = forms.CharField(max_length=100)
    mensagem = forms.CharField()
    email = forms.EmailField()
    
    
