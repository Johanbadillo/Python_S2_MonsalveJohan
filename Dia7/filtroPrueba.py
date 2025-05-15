
import json

def abrirJSON():
    dicFinal={}
    with open(".data.json",'w') as openFile:
        dicFinal=json.load(openFile)


for i in range(len(abrirJSON())):
    print(i)