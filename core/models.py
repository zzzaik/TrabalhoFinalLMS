from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError('RA precisa ser preenchido')
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, ra, password=None, **extra_fields):
        return self._create_user(ra, password, **extra_fields)

    def create_superuser(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)
    

class Usuario(AbstractBaseUser):
    nome = models.CharField('Nome', max_length=100, blank=True)
    ra = models.IntegerField('RA', unique=True)
    password = models.CharField(max_length=150)
    user_type = models.CharField(
        'Tipo de usuário', max_length=1, default='C')
    ativo = models.BooleanField('Ativo', default=True)
    email = models.EmailField('E-mail', unique=True)

    def __str__(self):
        return self.nome

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.user_type == 'C'

    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome', 'email']
    objects = UsuarioManager()


class Cursos(models.Model):
    sigla_curso = models.CharField(unique=True, max_length=5)
    nome_curso = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'cursos'

    def __str__(self):
        return self.nome_curso


class Disciplina(models.Model):
    nome_disciplina = models.CharField(
        unique=True, max_length=240, blank=True, null=True)
    carga_horaria = models.SmallIntegerField(blank=True, null=True)
    teoria_disciplina = models.DecimalField(
        max_digits=3, decimal_places=0, blank=True, null=True)
    pratica_disciplina = models.DecimalField(
        max_digits=3, decimal_places=0, blank=True, null=True)
    # This field type is a guess.
    ementa_disciplina = models.TextField(blank=True, null=True)
    # This field type is a guess.
    competencias_disciplina = models.TextField(blank=True, null=True)
    # This field type is a guess.
    habilidades_disciplina = models.TextField(blank=True, null=True)
    # This field type is a guess.
    conteudo_disciplina = models.TextField(blank=True, null=True)
    # This field type is a guess.
    bibliografia_basica_disciplina = models.TextField(blank=True, null=True)
    # This field type is a guess.
    bibliografia_complementar_disciplina = models.TextField(
        blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina'

    def __str__(self):
        return self.nome_disciplina


class GradeCurricular(models.Model):
    sigla_curso = models.ForeignKey(
        Cursos, models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    ano_grade = models.SmallIntegerField(blank=True, null=True)
    semestre_grade = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grade_curricular'
        unique_together = (('sigla_curso', 'ano_grade', 'semestre_grade'),)

    def __str__(self):
        return self.semestre_grade


class Periodo(models.Model):
    sigla_curso = models.ForeignKey(
        Cursos, models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    ano_grade = models.ForeignKey(
        GradeCurricular, models.DO_NOTHING, db_column='ano_grade', blank=True, null=True, related_name='+')
    semestre_grade = models.ForeignKey(
        GradeCurricular, models.DO_NOTHING, db_column='semestre_grade', blank=True, null=True, related_name='+')
    numero_periodo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo'
        unique_together = (('sigla_curso', 'ano_grade',
                            'semestre_grade', 'numero_periodo'),)


class Aluno(Usuario):
    parent_link = models.OneToOneField(
        Usuario, primary_key=True, db_column='user_id', parent_link=True)
    curso = models.ForeignKey(Cursos, blank=True, null=False)
    celular = models.CharField('Celular', max_length=11, null=False)
    semestre = models.IntegerField('Semestre', null=False)

    def __str__(self):
        return self.nome


class Professor(Usuario):
    parent_link = models.OneToOneField(
        Usuario, primary_key=True, db_column='user_id', parent_link=True)
    celular = models.CharField('Celular', max_length=11, null=True)
    apelido = models.CharField(
        'Apelido', max_length=30, null=False, unique=True)

    def __str__(self):
        return self.nome


class PeriodoDisciplina(models.Model):
    sigla_curso = models.ForeignKey(
        Cursos, models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    ano_grade = models.ForeignKey(GradeCurricular, models.DO_NOTHING,
                                  db_column='ano_grade', blank=True, null=True, related_name='+')
    semestre_grade = models.ForeignKey(
        GradeCurricular, models.DO_NOTHING, db_column='semestre_grade', blank=True, null=True, related_name='+')
    numero_periodo = models.IntegerField(blank=True, null=True)
    nome_disciplina = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo_disciplina'
        unique_together = (('sigla_curso', 'ano_grade',
                            'semestre_grade', 'numero_periodo', 'nome_disciplina'),)


class DisciplinaOfertada(models.Model):
    nome_disciplina = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_disciplina_ofertada = models.SmallIntegerField(blank=True, null=True)
    semestre_disciplina_ofertada = models.CharField(
        max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina_ofertada'
        unique_together = (
            ('nome_disciplina', 'ano_disciplina_ofertada', 'semestre_disciplina_ofertada'),)

    def __str__(self):
        return str(self.nome_disciplina)

class Turma(models.Model):
    nome_disciplina = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING,
                                     db_column='ano_ofertado', blank=True, null=True, related_name='+')
    semestre_ofertado = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True, related_name='+')
    id_turma = models.CharField(
        unique=True, max_length=1, blank=True, null=True)
    turno = models.CharField(max_length=15, blank=True, null=True)
    ra_professor = models.ForeignKey(
        Professor, models.DO_NOTHING, db_column='ra_professor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turma'
        unique_together = (
            ('nome_disciplina', 'ano_ofertado', 'semestre_ofertado'),)

    
class Matricula(models.Model):
    ra_aluno = models.ForeignKey(
        Aluno, models.DO_NOTHING, db_column='ra_aluno', blank=True, null=True)
    nome_disciplina = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING,
                                     db_column='ano_ofertado', blank=True, null=True, related_name='+')
    semestre_ofertado = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True, related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matricula'
        unique_together = (('ra_aluno', 'nome_disciplina',
                            'ano_ofertado', 'semestre_ofertado', 'id_turma'),)


class CursoTurma(models.Model):
    sigla_curso = models.ForeignKey(
        'Cursos', models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    nome_disciplina = models.ForeignKey(
        'Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING,
                                     db_column='ano_ofertado', blank=True, null=True, related_name='+')
    semestre_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True, related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso_turma'
        unique_together = (('sigla_curso', 'nome_disciplina',
                            'ano_ofertado', 'semestre_ofertado', 'id_turma'),)


class Questao(models.Model):
    nome_disciplina = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING,
                                     db_column='ano_ofertado', blank=True, null=True, related_name='+')
    semestre_ofertado = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True, related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)
    numero_questao = models.IntegerField(blank=True, null=True)
    data_limite_entrega = models.CharField(
        max_length=10, blank=True, null=True)
    # This field type is a guess.
    descricao = models.TextField(blank=True, null=True)
    data = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questao'
        unique_together = (('nome_disciplina', 'ano_ofertado',
                            'semestre_ofertado', 'id_turma', 'numero_questao'),)


class ArquivoQuestao(models.Model):
    nome_disciplina = models.ForeignKey(
        'Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING,
                                     db_column='ano_ofertado', blank=True, null=True, related_name='+')
    semestre_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True, related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)
    numero_questao = models.ForeignKey(
        'Questao', models.DO_NOTHING, db_column='numero_questao', blank=True, null=True)
    arquivo_questao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivo_questao'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado',
                            'id_turma', 'numero_questao', 'arquivo_questao'),)


class Resposta(models.Model):
    nome_disciplina = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING,
                                     db_column='ano_ofertado', blank=True, null=True, related_name='+')
    semestre_ofertado = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True, related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)
    numero_questao = models.ForeignKey(
        Questao, models.DO_NOTHING, db_column='numero_questao', blank=True, null=True)
    ra_aluno = models.IntegerField(blank=True, null=True)
    data_avaliacao = models.CharField(max_length=10, blank=True, null=True)
    nota = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    # This field type is a guess.
    avaliacao = models.TextField(blank=True, null=True)
    # This field type is a guess.
    descricao = models.TextField(blank=True, null=True)
    data_de_envio = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resposta'
        unique_together = (('nome_disciplina', 'ano_ofertado',
                            'semestre_ofertado', 'id_turma', 'numero_questao', 'ra_aluno'),)


class ArquivoResposta(models.Model):
    nome_disciplina = models.ForeignKey(
        'Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING,
                                     db_column='ano_ofertado', blank=True, null=True, related_name='+')
    semestre_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True, related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)
    numero_questao = models.ForeignKey(
        'Questao', models.DO_NOTHING, db_column='numero_questao', blank=True, null=True)
    ra_aluno = models.ForeignKey(
        'Aluno', models.DO_NOTHING, db_column='ra_aluno', blank=True, null=True)
    arquivo_resposta = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivo_resposta'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado',
                            'id_turma', 'numero_questao', 'ra_aluno', 'arquivo_resposta'),)


class CodigoMatricula(models.Model):
    id_aluno = models.ForeignKey('Aluno', models.DO_NOTHING, db_column='id_aluno')
    sigla_curso = models.CharField(max_length=5)
    codigo = models.CharField(max_length=10)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'codigo_matricula'
        unique_together = (('id_aluno', 'sigla_curso', 'codigo'),)
