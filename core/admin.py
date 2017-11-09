from django.contrib import admin
from core.models import Aluno, Professor, Curso, Disciplina
from django.contrib.auth.admin import UserAdmin
from django import forms


class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('ra', 'nome', 'email', 'celular', 'curso')

    def save(self, commit=True):
        user = super(NovoAlunoForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.user_type = 'A'
        if commit:
            user.save()
        return user


class AlterarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('email', 'nome', 'curso', 'celular')


class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('ra', 'nome', 'curso', 'email', 'celular')
    list_filter = ('user_type',)
    fieldsets = ((None, {'fields': ('email', 'nome', 'curso')}),)
    add_fieldsets = (
        (None, {'fields': ('ra', 'email', 'nome', 'curso', 'celular')}),)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Aluno, AlunoAdmin)


class NovoProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('ra', 'email',
                  'nome', 'apelido', 'celular')

    def save(self, commit=True):
        user = super(NovoProfessorForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.user_type = 'P'
        if commit:
            user.save()
        return user


class AlterarProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('email', 'nome', 'apelido', 'celular')


class ProfessorAdmin(UserAdmin):
    form = AlterarProfessorForm
    add_form = NovoProfessorForm
    list_display = ('nome', 'apelido', 'email')
    list_filter = ('user_type',)
    fieldsets = (
        (None, {'fields': ('email', 'nome', 'apelido')}),)
    add_fieldsets = ((None, {'fields': (
        'ra', 'email', 'nome', 'apelido', 'celular')}),)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Professor, ProfessorAdmin)

admin.site.register(Curso)
admin.site.register(Disciplina)
