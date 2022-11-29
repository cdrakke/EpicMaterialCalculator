import json, os
from pydoc import ispath

class DataManager:
    def __init__(self):
        self.filedirectory = "data"
        self.filepath = self.filedirectory + "/save.json"
        self.checkIfFileExists()

    def checkIfFileExists(self):
        if not os.path.isdir(self.filedirectory):
            os.mkdir('data')
            if not os.path.isfile(self.filepath):
                with open(self.filepath, 'w+') as writeFile:
                    data = {}
                    json.dump(data, writeFile, indent=4)

    def readData(self):
        with open(self.filepath, 'r') as readFile:
            data = json.load(readFile)
            return data
    
    def saveData(self, data):
        rdata = self.readData()
        if rdata == {}:
            struct = {
                "Scale": {},
                "Leather": {},
                "Horn": {}
            }
            if data["materialType"] == "Scale":
                struct["Scale"] = data
            elif data["materialType"] == "Leather":
                struct["Leather"] = data
            elif data["materialType"] == "Horn":
                struct["Horn"] = data

            with open(self.filepath, 'w') as writeFile:
                json.dump(struct, writeFile, indent=4)
        else:
            if data["materialType"] == "Scale":
                rdata["Scale"] = data
            elif data["materialType"] == "Leather":
                rdata["Leather"] = data
            elif data["materialType"] == "Horn":
                rdata["Horn"] = data

            with open(self.filepath, 'w') as writeFile:
                json.dump(rdata, writeFile, indent=4)

        
        
                    
