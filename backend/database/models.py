from django.db import models


class HeartBeat(models.Model):
    class Meta:
        db_table = 'heartbeat'
    datetime = models.DateTimeField()
    uptime = models.TextField()
    heap = models.FloatField()
    fps = models.FloatField()
    players = models.IntegerField()


class Player(models.Model):
    class Meta:
        db_table = 'players'
    steam_id = models.CharField(max_length=23, unique=True)
    nick_name = models.CharField(max_length=256)


class Playfield(models.Model):
    class Meta:
        db_table = 'playfields'
    name = models.CharField(max_length=64)


class PlayerTransferEvent(models.Model):
    class Meta:
        db_table = 'player_transfers'
    datetime = models.DateTimeField()
    player = models.ForeignKey(Player, to_field='steam_id') #  cos player can change nickname
    playfield = models.ForeignKey(Playfield)
    action = models.IntegerField() # 0 means went form, 1 means went to


class PlayerLogonEvent(models.Model):
    class Meta:
        db_table = 'player_logons'
    datetime = models.DateTimeField()
    player = models.ForeignKey(Player, to_field='steam_id')
    action = models.IntegerField()  # 0 - asked for login, 1 - logged in, 2 - logged out

class ChatMessage(models.Model):
    class Meta:
        db_table = 'chat'
    datetime = models.DateTimeField()
    player = models.ForeignKey(Player, to_field='steam_id')
    message = models.CharField(max_length=1024)