# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CoreAluno(models.Model):
    ra = models.ForeignKey('CoreUsuario', models.DO_NOTHING, db_column='ra', primary_key=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    curso = models.ForeignKey('Curso', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_aluno'


class CoreProfessor(models.Model):
    ra = models.ForeignKey('CoreUsuario', models.DO_NOTHING, db_column='ra', primary_key=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    apelido = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'core_professor'


class CoreUsuario(models.Model):
    last_login = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(max_length=100)
    ra = models.IntegerField(unique=True)
    password = models.CharField(max_length=150)
    user_type = models.CharField(max_length=1)
    ative = models.BooleanField()
    email = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'core_usuario'


class Curso(models.Model):
    sigla_curso = models.CharField(unique=True, max_length=5)
    nome_curso = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'curso'


class Disciplina(models.Model):
    nome_disciplina = models.CharField(unique=True, max_length=240)
    carga_horaria = models.SmallIntegerField()
    teoria_disciplina = models.DecimalField(max_digits=3, decimal_places=0)
    pratica_disciplina = models.DecimalField(max_digits=3, decimal_places=0)
    ementa_disciplina = models.TextField(blank=True, null=True)
    competencias_disciplina = models.TextField(blank=True, null=True)
    habilidades_disciplina = models.TextField(blank=True, null=True)
    conteudo_disciplina = models.TextField(blank=True, null=True)
    bibliografia_basica_disciplina = models.TextField(blank=True, null=True)
    bibliografia_complementar_disciplina = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(CoreUsuario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gradecurricular(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    ano_grade = models.SmallIntegerField(blank=True, null=True)
    semestre_grade = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gradecurricular'
        unique_together = (('sigla_curso', 'ano_grade', 'semestre_grade'),)


class Periodo(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    ano_grade = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='ano_grade', blank=True, null=True)
    semestre_grade = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='semestre_grade', blank=True, null=True)
    numero_periodo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo'
        unique_together = (('sigla_curso', 'ano_grade', 'semestre_grade', 'numero_periodo'),)
