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


class Professor(Usuario):
    parent_link = models.OneToOneField(
        Usuario, primary_key=True, db_column='user_id', parent_link=True)
    celular = models.CharField('Celular', max_length=11, null=True)
    apelido = models.CharField(
        'Apelido', max_length=30, null=False, unique=True)


class Curso(models.Model):
    sigla_curso = models.CharField(unique=True, max_length=5)
    nome_curso = models.CharField(unique=True, max_length=50)
    
    class Meta:
        managed = False
        db_table = 'curso'

    def __str__(self):
        return self.nome_curso


class GradeCurricular(models.Model):
    sigla_curso = models.ForeignKey(
        Curso, models.DO_NOTHING, db_column='sigla_curso')
    ano = models.SmallIntegerField()
    quantidade_semestre = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'grade_curricular'
        unique_together = (('sigla_curso', 'ano', 'quantidade_semestre'),)

    def __str__(self):
        return self.ano


class Periodo(models.Model):
    sigla_curso = models.ForeignKey(
        Curso, models.DO_NOTHING, db_column='sigla_curso')
    ano_grade = models.ForeignKey(
        GradeCurricular, models.DO_NOTHING, db_column='ano_grade', related_name='+')
    quantidade_semestre = models.ForeignKey(
        GradeCurricular, models.DO_NOTHING, db_column='quantidade_semestre', related_name='+')
    numero_periodo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'periodo'
        unique_together = (('sigla_curso', 'ano_grade',
                            'quantidade_semestre', 'numero_periodo'),)


class Disciplina(models.Model):
    nome_disciplina = models.CharField(unique=True, max_length=240)
    carga_horaria = models.SmallIntegerField()
    aula_teorica = models.DecimalField(max_digits=3, decimal_places=0)
    aula_pratica = models.DecimalField(max_digits=3, decimal_places=0)
    # This field type is a guess.
    ementa = models.TextField(blank=True, null=True)
    # This field type is a guess.
    competencias = models.TextField(blank=True, null=True)
    # This field type is a guess.
    habilidades = models.TextField(blank=True, null=True)
    # This field type is a guess.
    conteudo = models.TextField(blank=True, null=True)
    # This field type is a guess.
    bibliografia_basica = models.TextField(blank=True, null=True)
    # This field type is a guess.
    bibliografia_complementar = models.TextField(blank=True, null=True)
    periodo = models.ManyToManyField(to=Periodo, through='PeriodoDisciplina')

    class Meta:
        managed = False
        db_table = 'disciplina'

    def __str__(self):
        return self.nome_disciplina


class DisciplinaOfertada(models.Model):
    nome_disciplina = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column='nome_disciplina')
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'disciplina_ofertada'
        unique_together = (('nome_disciplina', 'ano', 'semestre'),)

    def __str__(self):
        return '%s  $s  %s' % (self.nome_disciplina, self.ano, self.semestre)


class Turma(models.Model):
    nome_disciplina = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado', related_name='+')
    semestre_ofertado = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', related_name='+')
    id_turma = models.CharField(max_length=2)
    turno = models.CharField(max_length=15)
    ra_professor = models.ForeignKey(
        Professor, models.DO_NOTHING, db_column='ra_professor')
    curso = models.ManyToManyField(to=Curso, through='CursoTurma')

    class Meta:
        managed = False
        db_table = 'turma'
        unique_together = (('nome_disciplina', 'ano_ofertado',
                            'semestre_ofertado', 'id_turma'),)

    def __str__(self):
        return self.num_turma


class CursoTurma(models.Model):
    sigla_curso = models.ForeignKey(
        Curso, models.DO_NOTHING, db_column='sigla_curso')
    nome_disciplina = models.ForeignKey(
        'Disciplina', models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='ano_ofertado', related_name='+')
    semestre_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado', related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma')

    class Meta:
        managed = False
        db_table = 'curso_turma'
        unique_together = (('sigla_curso', 'nome_disciplina',
                            'ano_ofertado', 'semestre_ofertado', 'id_turma'),)


class Aluno(Usuario):
    parent_link = models.OneToOneField(
        Usuario, primary_key=True, db_column='user_id', parent_link=True)
    curso = models.ForeignKey(Curso, blank=True, null=False)
    celular = models.CharField('Celular', max_length=11, null=False)
    semestre = models.IntegerField('Semestre', null=False, default=1)
    turma = models.ManyToManyField(to=Turma, through='Matricula')


class Matricula(models.Model):
    ra_aluno = models.ForeignKey(
        Aluno, models.DO_NOTHING, db_column='ra_aluno')
    nome_disciplina = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado', related_name='+')
    semestre_ofertado = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma')

    class Meta:
        managed = False
        db_table = 'matricula'
        unique_together = (('ra_aluno', 'nome_disciplina',
                            'ano_ofertado', 'semestre_ofertado', 'id_turma'),)


class PeriodoDisciplina(models.Model):
    sigla_curso = models.ForeignKey(
        Curso, models.DO_NOTHING, db_column='sigla_curso')
    ano_grade = models.ForeignKey(
        GradeCurricular, models.DO_NOTHING, db_column='ano_grade', related_name='+')
    quantidade_semestre = models.ForeignKey(
        GradeCurricular, models.DO_NOTHING, db_column='quantidade_semestre', related_name='+')
    numero_periodo = models.ForeignKey(
        Periodo, models.DO_NOTHING, db_column='numero_periodo')
    nome_disciplina = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column='nome_disciplina')
    
    class Meta:
        managed = False
        db_table = 'periodo_disciplina'
        unique_together = (('sigla_curso', 'ano_grade',
                            'quantidade_semestre', 'numero_periodo', 'nome_disciplina'),)


class Questao(models.Model):
    nome_disciplina = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado', related_name='+')
    semestre_ofertado = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma')
    numero_questao = models.IntegerField()
    data_limite = models.DateTimeField(blank=True, null=True)
    # This field type is a guess.
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'questao'
        unique_together = (('nome_disciplina', 'ano_ofertado',
                            'semestre_ofertado', 'id_turma', 'numero_questao'),)


class Resposta(models.Model):
    nome_disciplina = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='ano_ofertado', related_name='+')
    semestre_ofertado = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='semestre_ofertado', related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma')
    numero_questao = models.ForeignKey(
        Questao, models.DO_NOTHING, db_column='numero_questao')
    ra_aluno = models.ForeignKey(
        Aluno, models.DO_NOTHING, db_column='ra_aluno')
    data_avaliacao = models.CharField(max_length=10, blank=True, null=True)
    nota = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    # This field type is a guess.
    avaliacao = models.TextField(blank=True, null=True)
    # This field type is a guess.
    descricao = models.TextField(blank=True, null=True)
    data_envio = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'resposta'
        unique_together = (('nome_disciplina', 'ano_ofertado',
                            'semestre_ofertado', 'id_turma', 'numero_questao', 'ra_aluno'),)


def monta_arquivo_questao(questao, nome_arquivo):
    return '{}/{}/{}/{}'.format('questoes', questao.curso.sigla_curso, questao.numero_questao, nome_arquivo)


def monta_arquivo_resposta(resposta, nome_arquivo):
    return '{}/{}/{}/{}'.format('respostas', resposta.curso.sigla_curso, resposta.numero_questao, nome_arquivo)


class ArquivoQuestao(models.Model):
    nome_disciplina = models.ForeignKey(
        'Disciplina', models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='ano_ofertado', related_name='+')
    semestre_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado', related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma')
    numero_questao = models.IntegerField()
    arquivo_questao = models.FileField(upload_to=monta_arquivo_questao)

    class Meta:
        managed = False
        db_table = 'arquivo_questao'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado',
                            'id_turma', 'numero_questao', 'arquivo_questao'),)


class ArquivoResposta(models.Model):
    nome_disciplina = models.ForeignKey(
        'Disciplina', models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='ano_ofertado', related_name='+')
    semestre_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado', related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma')
    numero_questao = models.ForeignKey(
        'Questao', models.DO_NOTHING, db_column='numero_questao')
    ra_aluno = models.ForeignKey(
        'Aluno', models.DO_NOTHING, db_column='ra_aluno')
    arquivo_resposta = models.FileField(upload_to=monta_arquivo_resposta)

    class Meta:
        managed = False
        db_table = 'arquivo_resposta'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado',
                            'id_turma', 'numero_questao', 'ra_aluno', 'arquivo_resposta'),)
