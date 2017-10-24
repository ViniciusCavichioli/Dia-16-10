from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from lpc_evento.models import Pessoa, Evento, Ticket, Inscricao

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many = True)
    class Meta:
        model = Pessoa
        fields = ('nome', 'email', 'sexo', 'idade', 'usuario')

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('nome', 'dataEHoraDeInicio','endereco','logotipo','sigla','eventoPrincipal')

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    idEvento = EventoSerializer(many = True)
    class Meta:
        model = Ticket
        fields = ('nome', 'descricao','valor','idEvento')

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    Evento = EventoSerializer(many = True)
    Participante = PessoaSerializer(many = True)
    Ticket = TicketSerializer(many = True)
    class Meta:
        model = Inscricao
        fields = ('Evento', 'Participante','Ticket','validacao')
