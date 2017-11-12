# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CursoTurma(models.Model):
    sigla_curso = models.ForeignKey('Cursos', models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='ano_ofertado', blank=True, null=True)
    semestre_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True)
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso_turma'
        unique_together = (('sigla_curso', 'nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma'),)


class ArquivoResposta(models.Model):
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='ano_ofertado', blank=True, null=True)
    semestre_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True)
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)
    numero_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='numero_questao', blank=True, null=True)
    ra_aluno = models.ForeignKey('CoreAluno', models.DO_NOTHING, db_column='ra_aluno', blank=True, null=True)
    arquivo_resposta = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivo_resposta'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao', 'ra_aluno', 'arquivo_resposta'),)


class ArquivoQuestao(models.Model):
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='ano_ofertado', blank=True, null=True)
    semestre_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True)
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)
    numero_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='numero_questao', blank=True, null=True)
    arquivo_questao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivo_questao'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao', 'arquivo_questao'),)
