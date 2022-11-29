
class TeamView:
    
    def getTeam(self):
        team = input("Please Enter A Team, Enter q to go back to the main menu:")
        return team

    def displayTeam(self, team):
        
        if team == 0:
            print("Could not get information at this time, please try again later\n")
        
        elif team == 1:
            print("Team not found, please enter a valid team\n")

        else: 
            
            outputStr = "|{0:10s}|-----|{1:15s}|-----|{2:10s}|-----|{3:14s}|-----|{4:6s}|-----|{5:6s}|-----|{6:3}|-----|{7:8s}|"
            
            print(outputStr.format("First Name", "Last Name", "DOB", "Country", "Height", "Weight", "No.", "Position"))
            for player in team:
                print(outputStr.format(*player))
