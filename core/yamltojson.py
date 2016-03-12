#external dependency: http://pyyaml.org/wiki/PyYAML
#breaks comments!!!
from yaml import load_all, safe_dump
from yaml import CLoader as Loader
import json

class yamltojson():
    def __init__(self):
        pass

    def parseyaml(self,yamlstr):
        cnt = 0
        jsonstr=""
        for d in load_all(yamlstr, Loader=Loader):
            if cnt > 0: jsonstr+=(",\n")
            jsonstr+=(json.dumps(d, indent=4, sort_keys=True))
            cnt += 1
        return jsonstr
    def saveyaml(self,jsonstr):
        return safe_dump(json.loads(jsonstr), default_flow_style=False)

#yjs=yamltojson()
#print yamltojson.parseyaml(yjs,"# Playfield Characteristics\nRealRadius: 1303.797294             # Please don't change\nScaledRadius: 1300                  # Please don't change\nGravity: -10.1                      # Gravity on planet")
#print yamltojson.saveyaml(yjs,'{\n    "Gravity": -10.1,\n    "RealRadius": 1303.797294,\n    "ScaledRadius": 1300\n}')