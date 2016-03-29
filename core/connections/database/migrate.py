"""
creating tables in selected database. launch this script in case of new database
"""
import models
import json
print "creating tables..."
models.Player.create_table()
models.Playfield.create_table()
models.CoreLog.create_table()
models.HeartBeat.create_table()
models.PlayerLogonEvent.create_table()
models.PlayerTransferEvent.create_table()
models.ChatMessage.create_table()

PLAYFIELDS = (
    {
        "name": "Aestus Orbit",
        "folder": "SpaceAsteroidFieldRingAestus",
        "params": {"PvP": False}
    },
    {
        "name": "Aestus",
        "folder": "Lava",
        "params": {"PvP": True}
    },
    {
        "name": "Alien Outpost",
        "folder": "SpaceAlienStation",
        "params": {"PvP": True}
    },
    {
        "name": "Skillon Orbit",
        "folder": "SpaceAsteroidsFew",
        "params": {"PvP": False}
    },
    {
        "name": "Skillon",
        "folder": "Barren",
        "params": {"PvP": True}
    },
    {
        "name": "Trading Outpost",
        "folder": "SpaceTradingStation",
        "params": {"PvP": False}
    },
    {
        "name": "Akua Orbit",
        "folder": "SpaceAsteroidFieldRing",
        "params": {"PvP": False}
    },
    {
        "name": "Akua Moon",
        "folder": "Moon",
        "params": {"PvP": False}
    },
    {
        "name": "Omicron Orbit",
        "folder": "SpaceAsteroidFieldOmicron",
        "params": {"PvP": False}
    },
    {
        "name": "Omicron",
        "folder": "Desert",
        "params": {"PvP": False}
    },
    {
        "name": "Ningues Orbit",
        "folder": "SpaceEmptyNingues",
        "params": {"PvP": False}
    },
    {
        "name": "Ningues",
        "folder": "Snow",
        "params": {"PvP": True}
    },
    {
        "name": "Aitis Orbit",
        "folder": "SpaceAsteroids",
        "params": {"PvP": False}
    },
    {
        "name": "Aitis",
        "folder": "Lava2",
        "params": {"PvP": True}
    },
    {
        "name": "Asteroid Field",
        "folder": "SpaceAsteroidField",
        "params": {"PvP": True}
    },
    {
        "name": "Zeyhines Orbit",
        "folder": "SpaceAsteroidsFewZeyhines",
        "params": {"PvP": False}
    },
    {
        "name": "Zeyhines",
        "folder": "Desert2",
        "params": {"PvP": True}
    },
    {
        "name": "Masperon Orbit",
        "folder": "SpaceAsteroids",
        "params": {"PvP": False}
    },
    {
        "name": "Masperon",
        "folder": "Alien",
        "params": {"PvP": True}
    }
)
print "creating playfields..."
for pf in PLAYFIELDS:
    models.Playfield.create(
        name = pf['name'],
        folder = pf['folder'],
        params = json.dumps(pf['params'])
    )