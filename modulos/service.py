import sys
import os
from pathlib import Path
import json
from dataclasses import dataclass, asdict


ROOT = Path(__file__).parent
CONFIGURATION = "configuration.json"
PATHSAVE = Path.joinpath(ROOT, CONFIGURATION)


def readJson():
    if os.path.isfile(PATHSAVE):
        with open(PATHSAVE, "r") as f:
            return f.read()
    else:
        return None

def saveJson(pathName: str, jsonValid: str):
    pathName += ".json"
    # PATHSAVE = Path.joinpath(ROOT, pathName)
    
    dictTamplayt: dict

    if Path.is_file(PATHSAVE):
        j = readJson()
        if  j != None and j != "":
            dictTamplayt = json.loads(j)
            dictTamplayt["templayts"].append(json.loads(jsonValid))
        else:
            dictTamplayt = {"templayts": []}
            dictTamplayt["templayts"].append(json.loads(jsonValid))
    
        with open(PATHSAVE, "w") as f: # a = append 
            f.write(json.dumps(dictTamplayt))
        
        
        # with open(PATHSAVE, "r") as f: # a = append 
        #     fileText = f.read()
        #     if fileText != "":
        #         dictTamplayt = json.loads(fileText)
        #         dictTamplayt["templayts"].append(json.loads(jsonValid))
        #     else:
        #         dictTamplayt = {"templayts": []}
        #         dictTamplayt["templayts"].append(json.loads(jsonValid))
            

    else:
        with open(PATHSAVE, "w") as f: # a = append 
            dictTamplayt = {"templayts": []}
            dictTamplayt["templayts"].append(json.loads(jsonValid))
            f.write(json.dumps(dictTamplayt))

#deserializar======
# j= readJson("pysideCheckBoxPersonalit/modulos/teste.json")
# t = Templat(**j)
# print(t.mensagens[0])



# result= json.loads(modelo)
# j: dict
# j = readJson(PATHSAVE)
# if j != None:
#     k = j['templads']
#     print(type(k))
#     j['templads'].append({"mensage": "teste3"})
#     j['templads'].append({"mensage": "teste4"})

# r= json.dumps(j)
# saveJson(PATHSAVE, r)    