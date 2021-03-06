from django.contrib import admin
from core.models import *
from django.contrib.auth.admin import UserAdmin
from django import forms

class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('ra', 'nome', 'email', 'celular', 'curso', 'semestre', 'ano_ingresso')

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
        fields = ('email', 'nome', 'curso', 'celular', 'ativo', 'semestre', 'ano_ingresso', 'ativo')


class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('ra', 'nome', 'curso', 'email', 'celular', 'semestre', 'ano_ingresso', 'ativo')
    list_filter = ('user_type',)
    fieldsets = ((None, {'fields': ('email', 'nome', 'curso', 'semestre', 'ano_ingresso', 'ativo')}),)
    add_fieldsets = (
        (None, {'fields': ('ra', 'email', 'nome', 'curso', 'celular','semestre', 'ano_ingresso', 'ativo')}),)
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
        fields = ('email', 'nome', 'apelido', 'celular', 'ativo')


class ProfessorAdmin(UserAdmin):
    form = AlterarProfessorForm
    add_form = NovoProfessorForm
    list_display = ('nome', 'apelido', 'email', 'ativo')
    list_filter = ('user_type',)
    fieldsets = (
        (None, {'fields': ('email', 'nome', 'apelido', 'ativo')}),)
    add_fieldsets = ((None, {'fields': (
        'ra', 'email', 'nome', 'apelido', 'celular', 'ativo')}),)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
admin.site.register(Professor, ProfessorAdmin)

class NovoCoordenadorForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('ra', 'email',
                  'nome')

    def save(self, commit=True):
        user = super(NovoCoordenadorForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.user_type = 'C'
        if commit:
            user.save()
        return user


class AlterarCoordenadorForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('email', 'nome', 'ativo')

class CoordenadorAdmin(UserAdmin):
    form = AlterarCoordenadorForm
    add_form = NovoCoordenadorForm
    list_display = ('nome', 'email', 'ativo')
    list_filter = ('user_type',)
    fieldsets = (
        (None, {'fields': ('email', 'nome', 'ativo')}),)
    add_fieldsets = ((None, {'fields': (
        'ra', 'email', 'nome', 'ativo')}),)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
admin.site.register(Usuario, CoordenadorAdmin)

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(DisciplinaOfertada)
admin.site.register(Turma)
admin.site.register(GradeCurricular)
admin.site.register(Periodo)
admin.site.register(CursoTurma)
admin.site.register(PeriodoDisciplina)
