import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from prettytable import PrettyTable

class PlayerView:
    def promptUser(self):       #getting the user to input the name/teamid
        inp = []
        inp.append(input ("Enter the last name of the player you wish to search for (q to return to main menu): "))

        if(inp[0] == "q"):      #quit view
            return False

        print("\n Atl. Hawks: 1 \t\t\t Bos. Celtics: 2 \t Bro. Nets: 4 \t\t\t Cha. Hornets: 5 \t Chi. Bulls: 6 \n Cle. Cavaliers: 7 \t\t Dal. Mavericks: 8 \t Den. Nuggets: 9 \t\t Det. Pistons: 10 \t G.S. Warriors: 11 \n Hou. Rockets: 14 \t\t Ind. Pacers: 15 \t L.A. Clippers: 16 \t\t L.A. Lakers: 17 \t Mem. Grizzlies: 19 \n Mia. Heat: 20 \t\t\t Mil. Bucks: 21 \t Min. Timberwolves: 22 \t N.O. Pelicans: 23 \t N.Y. Knicks: 24 \n Okl. City Thunder: 25 \t Orl. Magic: 26 \t Phi. 76ers: 27 \t\t Phe. Suns: 28 \t\t Por. Trail Blazers: 29\n Sac. Kings: 30 \t\t S.A. Spurs: 31 \t Tor. Raptors: 38 \t\t Uta. Jazz: 40 \t\t Was. Wizards: 41 \n")
        inp.append(input("Enter the ID number of the team the player is on: "))

        if (inp[1] == "q"):     #quit view
            return False

        return inp

    def printPlayer(self, pArray):      #the found info is displayed or a warning
        if pArray == 0:
            print("Could not get information at this time, please try again later\n")

        elif pArray == 1:
            print("Player not found, please enter a valid last name/team ID combination\n")

        else:       #successful print
            
            playerTable = PrettyTable()
            playerTable.field_names = ["First Name", "Last Name", "DOB", "Country", "Height", "Weight", "No.", "Position"]

            for player in pArray:
                playerTable.add_row([*player])

            print(playerTable)
            input('Press return to continue\n')