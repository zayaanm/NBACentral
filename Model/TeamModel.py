#model class for the team option
class TeamModel:
    
    def __init__(self,ApiCaller):
        self.ApiCaller = ApiCaller

    #this is to clean the response of the API as the result it returns includes players that aren't active on the roster
    def getCurrentPlayers(self, players):
        
        #information for player that will be added to the new player array
        player = []
        #new player array that will be returned 
        playerArr = []
        
        for x in players:
            #if the player is an active player on the roster
            if x.get("nba").get("start") != 0 and "standard" in x.get("leagues") and x.get("leagues").get("standard").get("active") == True:
                player = []
                
                player.append(x.get("firstname"))
                player.append(x.get("lastname"))
                player.append(x.get("birth").get("date"))
                player.append(x.get("birth").get("country"))
                
                #if the player has valid information, the api result can include players that have been sent down to an affiliate league
                #in this case they would tecnically be considered an active player on the roster but practically theyre not, so we chose not to include them
                if x.get("height").get("feets") is not None and x.get("height").get("inches") is not None:
                    player.append(str(x.get("height").get("feets"))+"'"+str(x.get("height").get("inches")))
                else:
                    continue
                
                #look at previous comment for why this if statement was done
                if x.get("weight").get("pounds") is not None:
                    player.append(str(x.get("weight").get("pounds")))
                else:
                    continue
                
                #look at previous comment for why this if statement was done
                if x.get("leagues").get("standard").get("jersey") is not None:
                    player.append(x.get("leagues").get("standard").get("jersey"))
                else:
                    continue

                player.append(x.get("leagues").get("standard").get("pos"))
                playerArr.append(player)

        return playerArr

    #this is the method that the controller will use
    def getTeamPlayers(self, teamName):

        #the api we need uses team id to query, but we want the user to enter the name of the team, so we have to use this api to get the team id from the team name
        teamArr = self.ApiCaller.rapidApiCalltoDict("https://api-nba-v1.p.rapidapi.com/teams", {"name":str(teamName)})
        
        #if api doesnt work
        if teamArr == False:
            return 0

        #if team doesnt exist
        if len(teamArr.get("response")) == 0:
            return 1
        
        #get the team id and use it as a parameter in the next api call
        teamID = teamArr.get("response")[0].get("id")

        playerArr = self.ApiCaller.rapidApiCalltoDict("https://api-nba-v1.p.rapidapi.com/players", {"team":str(teamID),"season":"2021"})

        return self.getCurrentPlayers(playerArr.get("response"))

