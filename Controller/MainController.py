import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from Model.MainModel import MainModel
from View.MainView import MainView
from Controller.LeagueController import LeagueController
#from Controller.NewsController import NewsController



class MainController:

    def __init__(self):
        self.MainView = MainView()
        self.MainModel = MainModel()
        self.LeagueController = LeagueController()
        
        #self.NewsController = NewsController()


    def Menu(self):
        while(True):
            option = self.MainView.getUserOption()
            if option == '0':
                exit()
            self.selectController(option)


    def selectController(self, option):
        if option == '1':
            self.passToLeague()


    def passToLeague(self):
        self.LeagueController.showConferenceStats()


def main():
    mainController = MainController()
    mainController.Menu()


if __name__ == '__main__':
    main()

