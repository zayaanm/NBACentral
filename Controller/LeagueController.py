import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from View.LeagueView import LeagueView
from Model.LeagueModel import LeagueModel

class LeagueController:

    def __init__(self):
        self.LeagueView = LeagueView()
        self.LeagueModel = LeagueModel()

    def getData(self):
        year = self.LeagueView.getYearPrompt()
        if year == '0':
            return

        conference = self.LeagueView.getConferencePrompt()
        if conference == '0':
            return

        self.LeagueModel.findConferenceStats(year, conference)
        self.LeagueView.displayConferenceInfo(self.LeagueModel.getConferenceStats())