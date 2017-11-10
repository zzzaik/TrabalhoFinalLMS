# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Periododisciplina(models.Model):
    sigla_curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    ano_grade = models.ForeignKey('Gradecurricular', models.DO_NOTHING, db_column='ano_grade', blank=True, null=True)
    semestre_grade = models.ForeignKey('Gradecurricular', models.DO_NOTHING, db_column='semestre_grade', blank=True, null=True)
    numero_periodo = models.IntegerField(blank=True, null=True)
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periododisciplina'
        unique_together = (('sigla_curso', 'ano_grade', 'semestre_grade', 'numero_periodo', 'nome_disciplina'),)

class Disciplinaofertada(models.Model):
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_disciplina_ofertada = models.SmallIntegerField(blank=True, null=True)
    semestre_disciplina_ofertada = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplinaofertada'
        unique_together = (('nome_disciplina', 'ano_disciplina_ofertada', 'semestre_disciplina_ofertada'),)


class Turma(models.Model):
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='ano_ofertado', blank=True, null=True)
    semestre_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True)
    id_turma = models.CharField(unique=True, max_length=1, blank=True, null=True)
    turno = models.CharField(max_length=15, blank=True, null=True)
    ra_professor = models.ForeignKey('CoreProfessor', models.DO_NOTHING, db_column='ra_professor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turma'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado'),)


class Matricula(models.Model):
    ra_aluno = models.ForeignKey('CoreAluno', models.DO_NOTHING, db_column='ra_aluno', blank=True, null=True)
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='ano_ofertado', blank=True, null=True)
    semestre_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True)
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matricula'
        unique_together = (('ra_aluno', 'nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma'),)


class Cursoturma(models.Model):
    sigla_curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='ano_ofertado', blank=True, null=True)
    semestre_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True)
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cursoturma'
        unique_together = (('sigla_curso', 'nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma'),)


class Questao(models.Model):
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='ano_ofertado', blank=True, null=True)
    semestre_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True)
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma', blank=True, null=True)
    numero_questao = models.IntegerField(blank=True, null=True)
    data_limite_entrega = models.DateField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questao'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao'),)


class Arquivoquestao(models.Model):
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='ano_ofertado', blank=True, null=True)
    semestre_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True)
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)
    numero_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='numero_questao', blank=True, null=True)
    arquivo_questao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivoquestao'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao', 'arquivo_questao'),)


class Resposta(models.Model):
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='ano_ofertado', blank=True, null=True)
    semestre_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True)
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='id_turma', blank=True, null=True)
    numero_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='numero_questao', blank=True, null=True)
    ra_aluno = models.IntegerField(blank=True, null=True)
    data_avaliacao = models.DateField(blank=True, null=True)
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    avaliacao = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    data_de_envio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resposta'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao', 'ra_aluno'),)


class Arquivosresposta(models.Model):
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='ano_ofertado', blank=True, null=True)
    semestre_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True)
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)
    numero_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='numero_questao', blank=True, null=True)
    ra_aluno = models.ForeignKey('CoreAluno', models.DO_NOTHING, db_column='ra_aluno', blank=True, null=True)
    arquivo_resposta = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivosresposta'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao', 'ra_aluno', 'arquivo_resposta'),)
