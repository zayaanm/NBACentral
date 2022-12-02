import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from View.PlayerView import PlayerView
from Model.PlayerModel import PlayerModel

class PlayerController:

    def __init__(self,ApiCaller):
        self.pView = PlayerView()
        self.pMod = PlayerModel(ApiCaller)

    def namePrompt(self):
        self.inp = self.pView.promptUser()

    def setModel(self):
        self.pArray = self.pMod.setPlayer(self.inp)

    def printPlayer(self):
        self.pView.printPlayer(self.pArray)

    def getInput(self):
        return self.inp
    
    def showPlayer(self):
        self.namePrompt()
        self.setModel()
        self.printPlayer()



