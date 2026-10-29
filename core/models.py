from django.db import models 
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cpf = models.CharField('CPF', max_length=11)
    nascimento = models.DateField('Data de Nascimento')
    REQUIRED_FIELDS = ['cpf', 'nascimento']

class Area(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Publico(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Curso(models.Model):
    titulo = models.CharField('Titulo', max_length=200)
    descricao = models.TextField('Descricao', blank=True, null=True)
    vagas = models.IntegerField('Vagas')
    carga_horaria = models.IntegerField('Carga Horária')
    data = models.DateField('Data de Início')
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publico = models.ManyToManyField(Publico)

