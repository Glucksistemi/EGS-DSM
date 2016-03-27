"""
creating tables in selected database. launch this script in case of new database
"""
import models

models.Player.create_table()
models.Playfield.create_table()
models.CoreLog.create_table()
models.HeartBeat.create_table()
models.PlayerLogonEvent.create_table()
models.PlayerTransferEvent.create_table()
models.ChatMessage.create_table()