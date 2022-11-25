#from Model.LeagueModel import LeagueModel
import sys, os
sys.path.append(os.path.abspath(".."))
from View.LeagueView import LeagueView

class LeagueController:

    def __init__(self):
        self.LeagueView = LeagueView
        

    def prompt(self):
       self.LeagueView.displayMainMenu()

def main():
    league = LeagueController()
    league.prompt()

if __name__ == "__main__":
    main()