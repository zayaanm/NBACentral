import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from View.LeagueView import LeagueView
from Model.LeagueModel import LeagueModel

class LeagueController:

    def __init__(self):
        self.LeagueView = LeagueView()
        self.LeagueModel = LeagueModel()
        
    def menuPrompt(self):
       return self.LeagueView.displayMainMenu()

    def getData(self, dataOption):
        if dataOption == '1':
            self.LeagueModel.findPlayerStats()
            self.LeagueView.displayPlayerInfo(self.LeagueModel.getPlayerStats())

        elif dataOption == '2':
            year, conference = self.LeagueView.displayConferenceInfoPrompt()
            self.LeagueModel.findConferenceStats(year, conference)
            self.LeagueView.displayConferenceInfo(self.LeagueModel.getConferenceStats())

        else:
            print('err')


def main():
    league = LeagueController()
    option = league.menuPrompt()
    league.getData(option)

if __name__ == "__main__":
    main()