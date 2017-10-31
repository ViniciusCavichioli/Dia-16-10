from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from lpc_evento.models import Pessoa, Evento, Ticket, Inscricao

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many = False)
    class Meta:
        model = Pessoa
        fields = ('nome', 'email', 'sexo', 'idade', 'usuario')

    def create(self, dados):
        dados_usuario = dados.pop('usuario')
        U = User.objects.create(**dados_usuario)
        P = Pessoa.objects.create(usuario = U, **dados)
        return P

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('nome', 'dataEHoraDeInicio','endereco','logotipo','sigla','eventoPrincipal')

    def create(self, dados):
        return Evento.objects.create(**dados)

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    #idEvento = EventoSerializer(many = False)
    class Meta:
        model = Ticket
        fields = ('nome', 'descricao','valor','idEvento')

    def create(self, dados):
        E = dados.pop('idEvento')
        evento = Evento.objects.get(nome = E)
        T = Ticket.objects.create(idEvento = evento, **dados)
        return T

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    #Evento = EventoSerializer(many = False)
    #Participante = PessoaSerializer(many = False)
    #Ticket = TicketSerializer(many = False)
    class Meta:
        model = Inscricao
        fields = ('Evento', 'Participante','Ticket','validacao')

    def create(self, dados):
        dados_evento = dados.pop('Evento')
        dados_participante = dados.pop('Participante')
        dados_ticket = dados.pop('Ticket')
        E = Evento.objects.get(nome = dados_evento)
        P = Pessoa.objects.get(nome = dados_participante)
        T = Ticket.objects.get(nome = dados_ticket)
        I = Inscricao.objects.create(Evento = E, Participante = P, Ticket = T, **dados)
        return I
