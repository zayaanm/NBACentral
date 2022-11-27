import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from Model.MainModel import MainModel
from View.MainView import MainView
from Controller.LeagueController import LeagueController


class MainController:

    def __init__(self):
        self.controller = self
        self.option = 0

    def printMain():

        print('League stats')

    def printLeague():
        LeagueController.method()
        print('League stats')

    def printPlayer():
        print('League stats')

    def printNews():
        print('League stats')
