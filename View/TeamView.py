#View class for team option
from prettytable import PrettyTable

class TeamView:
    
    #Gets the user input for team they want information for
    def getTeam(self):
        team = input("Please enter a team. Enter q to go back to the main menu:")
        return team

    #displays the user-selected team, shows error message based on the error
    def displayTeam(self, team):
        
        #api called failed
        if team == 0:
            print("Could not get information at this time, please try again later\n")
        
        #api could not find user-selected team
        elif team == 1:
            print("Team not found, please enter a valid team\n")

        #api finds user-selected team and displays it
        else: 

            table = PrettyTable()
            table.field_names = ["First Name", "Last Name", "DOB", "Country", "Height", "Weight", "No.", "Position"]

            for player in team:
                table.add_row([*player])

            print(table)
