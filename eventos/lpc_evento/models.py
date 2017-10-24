from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length = 128)
    email = models.CharField(max_length = 100)
    sexo = models.CharField(max_length=10)
    idade = models.IntegerField()
    usuario = models.ForeignKey(User, null=True, blank=False)

class Evento(models.Model):
    nome = models.CharField(max_length = 100)
    dataEHoraDeInicio = models.DateField(max_length = 20)
    endereco = models.CharField(max_length = 150)
    logotipo = models.CharField(max_length=40)
    sigla = models.CharField(max_length=14)
    eventoPrincipal = models.CharField(max_length=256)

class Ticket(models.Model):
    nome = models.CharField(max_length = 128)
    descricao = models.TextField()
    valor = models.FloatField()
    idEvento = models.ForeignKey(Evento, related_name = 'Evento_Ticket', null = True, blank = False)

class Inscricao(models.Model):
    Evento = models.ForeignKey(Evento, related_name = 'Evento_Inscricao', null = True, blank = False)
    Participante = models.ForeignKey(Pessoa, related_name = 'Pessoa_Inscricao', null = True, blank = False)
    Ticket = models.ForeignKey(Ticket, related_name = 'Ticket_Inscricao', null = True, blank = False)
    validacao = models.CharField(max_length=40)
