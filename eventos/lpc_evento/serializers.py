from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from lpc_evento.models import Pessoa, Evento, Ticket, Inscricao

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('nome', 'email', 'sexo', 'idade', 'usuario')

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agenda
        fields = ('nome', 'dataEHoraDeInicio','endereco','logotipo','sigla','eventoPrincipal')

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    idEvento = EventoSerializer(many = True)
    class Meta:
        model = Agenda
        fields = ('nome', 'descricao','valor','idEvento')

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    idEvento = EventoSerializer(many = True)
    idParticipante = PessoaSerializer(many = True)
    idTicket = TicketSerializer(many = True)
    class Meta:
        model = Agenda
        fields = ('Evento', 'Participante','Ticket','validacao')
