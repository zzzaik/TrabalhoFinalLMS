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
        'Tipo de usuário', max_length=1, default = 'C')
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


class Curso(models.Model):
    sigla_curso = models.CharField(unique=True, max_length=5)
    nome_curso = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'curso'

    def __str__(self):
        return self.nome_curso


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
    bibliografia_complementar_disciplina = models.TextField(
        blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina'

    def __str__(self):
        return self.nome_disciplina


class Gradecurricular(models.Model):
    sigla_curso = models.ForeignKey(
        Curso, models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    ano_grade = models.SmallIntegerField(blank=True, null=True)
    semestre_grade = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gradecurricular'
        unique_together = (('sigla_curso', 'ano_grade', 'semestre_grade'),)


class Periodo(models.Model):
    sigla_curso = models.ForeignKey(
        Curso, models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    ano_grade = models.ForeignKey(
        Gradecurricular, models.DO_NOTHING, db_column='ano_grade', blank=True, null=True, related_name='+')
    semestre_grade = models.ForeignKey(
        Gradecurricular, models.DO_NOTHING, db_column='semestre_grade', blank=True, null=True, related_name='+')
    numero_periodo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo'
        unique_together = (('sigla_curso', 'ano_grade',
                            'semestre_grade', 'numero_periodo'),)


class Aluno(Usuario):
    parent_link = models.OneToOneField(Usuario, primary_key=True, db_column='user_id', parent_link=True)
    curso = models.ForeignKey(Curso, blank=True, null=False)
    celular = models.CharField('Celular', max_length=11, null=True)

    def __str__(self):
        return self.nome


class Professor(Usuario):
    parent_link = models.OneToOneField(Usuario, primary_key=True, db_column='user_id', parent_link=True)
    celular = models.CharField('Celular', max_length=11, null=True)
    apelido = models.CharField('Apelido', max_length=30, null=False, unique = True)

    def __str__(self):
        return self.nome
