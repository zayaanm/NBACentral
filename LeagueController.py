from Model.LeagueModel import LeagueModel
from View.LeagueView import LeagueView

class LeagueController:

    def __init__(self):
        self.LeagueView = LeagueView()
        self.LeagueModel = LeagueModel()
        self.option = 0
        
    def menuPrompt(self):
       self.option= self.LeagueView.displayMainMenu()
       return self.option

    def getData(self):
        if self.option == '1':
            self.LeagueModel.findPlayerStats()
        elif self.option == '2':
            self.LeagueModel.findConferenceStats()
        else:
            print('err')

    def displayData(self):
        if self.option == '1':
            self.LeagueView.displayPlayerInfo(self.LeagueModel.getPlayerStats())
        elif self.option == '2':
            self.LeagueView.displayConferenceInfo(self.LeagueModel.getConferenceStats())
        else:
            print('err')


def main():
    league = LeagueController()
    league.menuPrompt()
    league.getData()
    league.displayData()

if __name__ == "__main__":
    main()