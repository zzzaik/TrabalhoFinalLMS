from django.db import models

# Create your models here.
class Mensagem(models.Model):
    destinatario=models.CharField(max_length=12)
    remetente=models.CharField(max_length=12)
    curso=models.CharField(max_length=100)
    turma=models.CharField(max_length=100)
    mensagem=models.CharField(max_length=500)
    data_envio=models.DateTimeField()
