#Controller for Player View
#Aidan David (251083708)

from Model import PlayerModel
from View import PlayerView
class PlayerController:
    pMod = "x"
    pView = "x"
    inp = "x"

    def __init__(self):
        self.pView = PlayerView();
        self.inp = self.pView.search();
        self.pMod = PlayerModel(self.inp);

    def getName(self):
        return self.pView.name

    def getPosition(self):
        return self.pView.pos

    def getAge(self):
        return self.pView.age

    def getTeam(self):
        return self.pView.team

    def getNumber(self):
        return self.pView.num

    def getHeight(self):
        return self.pView.hght

    def getPoints(self):
        return self.pView.pts

    def getAssists(self):
        return self.pView.ats

    def getSteals(self):
        return self.pView.stls

    def getRebounds(self):
        return self.pView.rbs

    def getBlocks(self):
        return self.pView.blks

    def getTurnOvers(self):
        return self.pView.tos

    def getPlusMinus(self):
        return self.pView.pm