import sys
import os
from pathlib import Path
import json


ROOT = Path(__file__).parent
CONFIGURATION = "configuration.json"
PATHSAVE = Path.joinpath(ROOT, CONFIGURATION)


# {"templads": [
    
#     {"name": "conferencia", "mensage": ["teste1"]},
#     {"name": "confHD", "mensage": ["teste2", "teste2"]}

# ]}

def readJson(pathName: str):
    if os.path.isfile(pathName):
        with open(pathName) as f:
            return json.load(f)
        
def saveJson(pathName: str, jsonValid: str):
    with open(pathName, "w") as f: # a = append 
        f.write(jsonValid)

# result= json.loads(modelo)
j: dict
j = readJson(PATHSAVE)
if j != None:
    k = j['templads']
    print(type(k))
    j['templads'].append({"mensage": "teste3"})
    j['templads'].append({"mensage": "teste4"})

r= json.dumps(j)
saveJson(PATHSAVE, r)    