#View class for team option

class TeamView:
    
    #Gets the user input for team they want information for
    def getTeam(self):
        team = input("Please Enter A Team, Enter q to go back to the main menu:")
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
            
            #format string for the table
            outputStr = "|{0:10s}|-----|{1:15s}|-----|{2:10s}|-----|{3:14s}|-----|{4:6s}|-----|{5:6s}|-----|{6:3}|-----|{7:8s}|"
            
            #header for the table
            print(outputStr.format("First Name", "Last Name", "DOB", "Country", "Height", "Weight", "No.", "Position"))
            
            #printing out each player thats returned in the team list (which is a 2D array)
            for player in team:
                print(outputStr.format(*player))
