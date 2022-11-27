#Implementation of Player View
#Aidan David (251083708)

import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from Model.PlayerModel import PlayerModel

class PlayerView:
    def promptUser(self):
        inp = input ("Enter the name of the player you wish to search for: ")
        return inp

    def printPlayer(self, pMod):
        print("Name: " + pMod.getName())
        print("Position: " + pMod.getPosition())
        print("Age: " + pMod.getAge())
        print("Team: " + pMod.getTeam())
        print("Number: " + pMod.getNumber())
        print("Height: " + pMod.getHeight())
        print("Points: " + pMod.getPoints())
        print("Assists: " + pMod.getAssists())
        print("Steals: " + pMod.getSteals())
        print("Rebounds: " + pMod.getRebounds())
        print("Blocks: " + pMod.getBlocks())
        print("Turn Overs: " + pMod.getTurnOvers())
        print("Ples/Minus: " + pMod.getPlusMinus())