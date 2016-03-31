from utils.views import JsonView
from utils.models import *
from utils.tcpclient import tcp_request
from django.http import HttpResponseServerError


class ChatMessagesView(JsonView):
    def react(self, data):
        if 'last_id' in data:
            result = ChatMessage.objects.filter(id__gt=data['last_id'])
        else:
            result = ChatMessage.objects.all()[0:100]
        messages = []
        for message in result:
            messages.append({
                'id': message.id,
                'datetime': message.datetime.strftime('%d %m %Y, %H:%M:%S'),
                'player': message.player.nick_name,
                'text': message.message
            })
        return {'chat': messages}


class SendChatMessage(JsonView):
    def react(self, data):
        if 'message' not in data:
            return {'error': 'no incoming message'}
        try:
            return {
                'msg': tcp_request('chat '+ data['message'])
            }
        except:
            raise HttpResponseServerError


class PlayerInfo(JsonView):
    def react(self, data):
        players = Player.objects.all()
        response = []
        for player in players:
            logon = PlayerLogonEvent.objects.filter(player=player, action__in=[1,2]).latest('datetime')
            state = 'online' if logon.action == 1 else 'offline'
            # TODO: replace "online" with "banned" if player is banned by banned players check (via unwritten asker)
            playfield = PlayerTransferEvent.objects.filter(player=player, action=1).latest('datetime').playfield.name
            response.append({
                'steam_id': player.steam_id,
                'nick_name': player.nick_name,
                'state': state,
                'since': logon.datetime.strftime('%d.%m %H:%M'),
                'playfield': playfield
            })
        return response