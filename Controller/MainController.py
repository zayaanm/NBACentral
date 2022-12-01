import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from Model.MainModel import MainModel
from View.MainView import MainView
from Controller.LeagueController import LeagueController
from Controller.TeamController import TeamController
from Controller.NewsController import NewsController
from Controller.PlayerController import PlayerController



class MainController:

    def __init__(self):
        self.MainView = MainView()
        self.MainModel = MainModel()
        self.LeagueController = LeagueController()
        self.TeamController = TeamController()
        self.NewsController = NewsController()
        self.PlayerController = PlayerController()


    def Menu(self):
        while(True):
            option = self.MainView.getUserOption()
            if option == '0':
                exit()
            self.selectController(option)


    def selectController(self, option):
        if option == '1':
            self.passToLeague()
        elif option == '2':
            self.passToTeam()
        elif option == '3':
            self.passToNews()
        elif option == '4':
            self.passToPlayer()

    def passToLeague(self):
        self.LeagueController.showConferenceStats()

    def passToTeam(self):
        self.TeamController.controller()

    def passToNews(self):
        self.NewsController.showNews()
    
    def passToPlayer(self):
        self.PlayerController.showPlayer()

def main():
    mainController = MainController()
    mainController.Menu()

if __name__ == '__main__':
    main()


