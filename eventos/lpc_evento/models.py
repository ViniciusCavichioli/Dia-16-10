from django.db import models


class Usuario(models.Model):
    telefone = models.CharField(max_length = 11)
    
class Pessoa(models.Model):
    idUsuario = models.ForeignKey(Usuario, related_name = 'Usuario', null = True, blank = False)
    nome = models.CharField(max_length = 128)
    email = models.CharField(max_length = 100)

class Evento(models.Model):
    nome = models.CharField(max_length = 100)
    dataEHoraDeInicio = models.DateField(max_length = 20)
    endereco = models.CharField(max_length = 150)

class Ticket(models.Model):
    nome = models.CharField(max_length = 128)
    descricao = models.TextField()
    valor = models.Money()
    idEvento = models.ForeignKey(Eveto, related_name = 'Evento', null = True, blank = False)

class Inscricao(models.Model):
    idEvento = models.ForeignKey(Eveto, related_name = 'Evento', null = True, blank = False)
    idPesso = models.ForeignKey(Pessoa, related_name = 'Pessoa', null = True, blank = False)
    idTicket = models.ForeignKey(Ticket, related_name = 'Ticket', null = True, blank = False)
    validacao = models.CharField(max_length = 50)
