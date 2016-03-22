from models import Player, PlayerLogonEvent, PlayerTransferEvent, Playfield
import datetime


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
        player = Player.get(nick_name=nick_name)
    elif steam_id and not nick_name:
        return Player.get(steam_id=steam_id)
    elif steam_id and nick_name:
        try:
            player = Player.get(steam_id=steam_id)
        except Player.DoesNotExist:
            player = Player.create(steam_id=steam_id, nick_name=nick_name)
        if nick_name != player.nick_name:
            player.nick_name = nick_name  # TODO: test for it
        return player


def save_logon_event(action, nick_name='', steam_id=''):
    print 'logon_action'
    player = Player.get(nick_name=nick_name)
    PlayerLogonEvent.create(
        player_id=get_player(nick_name, steam_id),
        datetime=datetime.datetime.now(),
        action = action
    )


def save_playfield_change(action, nick_name='', steam_id='', playfield=''):
    player = get_player(nick_name, steam_id)

    PlayerTransferEvent.create(
        datetime=datetime.datetime.now(),
        player_id=player,
        playfield=Playfield.get(Playfield.name == playfield),
        action=action
    )