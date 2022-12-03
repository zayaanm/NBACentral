import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from View.PlayerView import PlayerView
from Model.PlayerModel import PlayerModel

class PlayerController:

    def __init__(self,ApiCaller):       #constructor
        self.pView = PlayerView()
        self.pMod = PlayerModel(ApiCaller)

    def namePrompt(self):               #gets user enter teh player name
        self.inp = self.pView.promptUser()

    def setModel(self):                 #sets the model to the specific player
        self.pArray = self.pMod.setPlayer(self.inp)

    def printPlayer(self):              #the player view prints the information
        self.pView.printPlayer(self.pArray)

    def getInput(self):                 #returns the user's input
        return self.inp
    
    def showPlayer(self):               #performs player as intended
        self.namePrompt()
        self.setModel()
        self.printPlayer()



