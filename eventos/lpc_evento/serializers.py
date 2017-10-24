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

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('nome', 'dataEHoraDeInicio','endereco','logotipo','sigla','eventoPrincipal')

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    idEvento = EventoSerializer(many = False)
    class Meta:
        model = Ticket
        fields = ('nome', 'descricao','valor','idEvento')

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    Evento = EventoSerializer(many = False)
    Participante = PessoaSerializer(many = False)
    Ticket = TicketSerializer(many = False)
    class Meta:
        model = Inscricao
        fields = ('Evento', 'Participante','Ticket','validacao')
