from peewee import MySQLDatabase, SqliteDatabase, PostgresqlDatabase, Model, DateTimeField, FloatField, IntegerField, ForeignKeyField, CharField, ImproperlyConfigured

db = MySQLDatabase('egsdsm', host='localhost', user='egsdsm', password='123QWErty')


def get_db(**kwargs):
    dbtype = {
        'mysql': MySQLDatabase,
        'sqlite': SqliteDatabase,
        'postgres': PostgresqlDatabase
    }
    try:
        db = dbtype[kwargs['type']](kwargs['name'], **kwargs['params'])
    except KeyError:
        raise ImproperlyConfigured

class HeartBeat(Model):
    class Meta:
        database = db
        db_table = 'heartbeat'
    datetime = DateTimeField()
    uptime = IntegerField()
    heap = FloatField()
    fps = FloatField()
    players = IntegerField()


class Player(Model):
    class Meta:
        database = db
        db_table = 'players'
    steam_id = CharField(max_length=23, unique=True)
    nick_name = CharField(max_length=256)


class Playfield(Model):
    class Meta:
        database = db
        db_table = 'playfields'
    name = CharField(max_length=64)


class PlayerTransferEvent(Model):
    class Meta:
        database = db
        db_table = 'player_transfers'
    datetime = DateTimeField()
    player = ForeignKeyField(Player, to_field='steam_id')  # cos player can change nickname
    playfield = ForeignKeyField(Playfield)
    action = IntegerField()  # 0 means went form, 1 means went to


class PlayerLogonEvent(Model):
    class Meta:
        database = db
        db_table = 'player_logons'
    datetime = DateTimeField()
    player_id = ForeignKeyField(Player, to_field='steam_id', related_name='logon_events')
    action = IntegerField()  # 0 - asked for login, 1 - logged in, 2 - logged out


class ChatMessage(Model):
    class Meta:
        database = db
        db_table = 'chat'
    datetime = DateTimeField()
    player = ForeignKeyField(Player, to_field='steam_id')
    message = CharField(max_length=1024)
