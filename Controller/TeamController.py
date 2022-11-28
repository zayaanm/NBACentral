import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from View.TeamView import TeamView
from Model.TeamModel import TeamModel

class TeamController():

    def __init__(self,view,model):
        self.view = view
        self.model = model

    def controller(self):
        
        userResponse = self.view.getTeam()

        while (userResponse != 'q'):

            teamPlayers = self.model.getTeamPlayers(userResponse)
            self.view.displayTeam(teamPlayers)
            userResponse = self.view.getTeam()

if __name__ == "__main__":
    view = TeamView()
    model = TeamModel()
    t = TeamController(view, model)
    t.controller()



