#Model For Player View
#Aidan David (251083708)

import json
import requests
import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

class PlayerModel:

    def __init__(self):
        pass

    def setPlayer(self, pName):

        per = {"name": str(pName), "team": "1", "season": "2021"}

        pArray = self.APICall(per)
        pArray = self.APICall(per)
        pArray = self.APICall(per)

        print(pArray)

        if(pArray == False):
            return False

        self.name = 'y'
        self.pos = "y"
        self.age = "y"
        self.team = "y"
        self.num = "y"
        self.hgt = "y"
        self.pts = "y"
        self.ats = "y"
        self.stls = "y"
        self.rbs = "y"
        self.blks = "y"
        self.tos = "y"
        self.pm = "y"

        return True

    def APICall(self, parameters):

        headers = {
            "X-RapidAPI-Key": "bc1b759fdfmshb77a2031d4430cbp1169cfjsn62a876e90d2a",
            "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
        }

        response = requests.get("https://api-nba-v1.p.rapidapi.com/players", headers=headers, params=parameters)
        print(response.text)

        if response.status_code != 200:
            return False

        pArray = json.loads(json.dumps(response.json()))

        return pArray

    def getName(self):
        return self.name

    def getPosition(self):
        return self.pos

    def getAge(self):
        return self.age

    def getTeam(self):
        return self.team

    def getNumber(self):
        return self.num

    def getHeight(self):
        return self.hgt

    def getPoints(self):
        return self.pts

    def getAssists(self):
        return self.ats

    def getSteals(self):
        return self.stls

    def getRebounds(self):
        return self.rbs

    def getBlocks(self):
        return self.blks

    def getTurnOvers(self):
        return self.tos

    def getPlusMinus(self):
        return self.pm