BEGIN;
CREATE TABLE "chat" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "datetime" datetime NOT NULL, "message" varchar(1024) NOT NULL);
CREATE TABLE "heartbeat" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "datetime" datetime NOT NULL, "uptime" text NOT NULL, "heap" real NOT NULL, "fps" real NOT NULL, "players" integer NOT NULL);
CREATE TABLE "players" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "steam_id" varchar(23) NOT NULL UNIQUE, "nick_name" varchar(256) NOT NULL);
CREATE TABLE "player_logons" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "datetime" datetime NOT NULL, "action" integer NOT NULL, "player_id" varchar(23) NOT NULL REFERENCES "players" ("steam_id"));
CREATE TABLE "player_transfers" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "datetime" datetime NOT NULL, "action" integer NOT NULL, "player_id" varchar(23) NOT NULL REFERENCES "players" ("steam_id"));
CREATE TABLE "playfields" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(64) NOT NULL);
CREATE TABLE "player_transfers__new" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "datetime" datetime NOT NULL, "action" integer NOT NULL, "player_id" varchar(23) NOT NULL REFERENCES "players" ("steam_id"), "playfield_id" integer NOT NULL REFERENCES "
playfields" ("id"));
INSERT INTO "player_transfers__new" ("action", "player_id", "id", "playfield_id", "datetime") SELECT "action", "player_id", "id", NULL, "datetime" FROM "player_transfers";
DROP TABLE "player_transfers";
ALTER TABLE "player_transfers__new" RENAME TO "player_transfers";
CREATE INDEX "player_logons_afe72417" ON "player_logons" ("player_id");
CREATE INDEX "player_transfers_afe72417" ON "player_transfers" ("player_id");
CREATE INDEX "player_transfers_7040caa8" ON "player_transfers" ("playfield_id");
CREATE TABLE "chat__new" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "datetime" datetime NOT NULL, "message" varchar(1024) NOT NULL, "player_id" varchar(23) NOT NULL REFERENCES "players" ("steam_id"));
INSERT INTO "chat__new" ("player_id", "message", "id", "datetime") SELECT NULL, "message", "id", "datetime" FROM "chat";
DROP TABLE "chat";
ALTER TABLE "chat__new" RENAME TO "chat";
CREATE INDEX "chat_afe72417" ON "chat" ("player_id");

COMMIT;
