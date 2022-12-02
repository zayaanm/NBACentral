import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from View.TeamView import TeamView
from Model.TeamModel import TeamModel

#controller class for the team option

class TeamController():

    def __init__(self,ApiCaller):
        self.view = TeamView()
        self.model = TeamModel(ApiCaller)

    #method that runs the class
    def controller(self):
        
        userResponse = self.view.getTeam()

        #q was selelcted to be the exit option, change to anything else if you would like
        #this while loop will keep displaying the user-selected teams until they would like to go back to the main menu
        while (userResponse != 'q'):

            teamPlayers = self.model.getTeamPlayers(userResponse)
            self.view.displayTeam(teamPlayers)
            userResponse = self.view.getTeam()


