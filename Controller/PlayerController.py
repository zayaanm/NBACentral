#Controller for Player View
#Aidan David (251083708)

import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from View.PlayerView import PlayerView
from Model.PlayerModel import PlayerModel

class PlayerController:

    def __init__(self):
        self.pView = PlayerView()
        self.pMod = PlayerModel()

    def namePrompt(self):
        self.inp = self.pView.promptUser()

    def setModel(self):
        self.worked = self.pMod.setPlayer(self.inp)

    def getInput(self):
        return self.inp

    def printPlayer(self):
        self.pView.printPlayer(self.pMod)

    def getWorked(self):
        return self.worked

cont = PlayerController()
cont.namePrompt()
cont.setModel()
if(cont.getWorked() == True):
    cont.printPlayer()

