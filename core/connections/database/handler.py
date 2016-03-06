from models import HeartBeat, Player, PlayerLogonEvent
import datetime


def save_heartbeat(uptime, heap, fps, players):
    HeartBeat.create(
        datetime = datetime.datetime.now(),
        uptime=uptime,
        heap=float(heap),
        fps=float(fps),
        players=int(players)
    )


def get_player(nick_name = '', steam_id = ''):
    """
    gets player by given params.
    If player changed nickname - replaces old one in db
    If no such player - creates new
    :param nick_name:
    :param steam_id:
    :param may_be_new:
    :return:Player object
    """
    if nick_name and not steam_id:
        return Player.get(Player.nick_name == nick_name)
    elif steam_id and not nick_name:
        return Player.get(Player.steam_id == steam_id)
    elif steam_id and nick_name: #  TODO: check for existing user with this steamID and replace his nick
        return Player.get_or_create(nick_name=nick_name, steam_id=steam_id)


def save_logon_event(action, nick_name='', steam_id=''):
    player = get_player(nick_name, steam_id)
    PlayerLogonEvent.create(
        player=player,
        datetime=datetime.datetime.now(),
        action = action
    )