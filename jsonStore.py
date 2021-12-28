import json 
from json.decoder import JSONDecodeError
from os.path import join, dirname

def addToJson(collectionName, apps):
    new_data = {collectionName : apps}
    with open('collections.json', 'r+') as outfile:
        try:
            json_data = json.load(outfile)
        except: 
            json_data = {}
            pass
        print(f"Collection name is {collectionName} and apps is\n{apps}")
        print(f"They are of types: {type(collectionName)} and {type(apps)}")
        json_data[collectionName] = apps
        outfile.seek(0)
        json.dump([json_data], outfile)

        
def returnAllCollections():
    data={}
    with open('collections.json') as outfile:
        try:
            data = json.load(outfile)
        except JSONDecodeError: 
            pass
    return data
    
def removeFromJson(collectionName, apps):
    pass

def renameCollection(collectionName):
    pass

def editCollection(collectionName):
    pass