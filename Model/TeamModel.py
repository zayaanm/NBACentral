import requests
import json


class TeamModel:
    
    def __init__(self):
        pass

    def makeApiCall(self, url, parameters):

        headers = {
            "X-RapidAPI-Key": "de229dde0cmsh61bafd93b3a54afp18db1djsn21ebcafe56ad",
            "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=parameters)

        if response.status_code != 200:
            return False

        arr = json.loads(json.dumps(response.json()))

        return arr

    def getCurrentPlayers(self, players):
        
        player = []
        playerArr = []
        for x in players:
            if x.get("nba").get("start") != 0 and "standard" in x.get("leagues") and x.get("leagues").get("standard").get("active") == True:
                player = []
                
                player.append(x.get("firstname"))
                player.append(x.get("lastname"))
                player.append(x.get("birth").get("date"))
                player.append(x.get("birth").get("country"))
                
                if x.get("height").get("feets") is not None and x.get("height").get("inches") is not None:
                    player.append(str(x.get("height").get("feets"))+"'"+str(x.get("height").get("inches")))
                else:
                    continue

                if x.get("weight").get("pounds") is not None:
                    player.append(str(x.get("weight").get("pounds")))
                else:
                    continue

                if x.get("leagues").get("standard").get("jersey") is not None:
                    player.append(x.get("leagues").get("standard").get("jersey"))
                else:
                    continue

                player.append(x.get("leagues").get("standard").get("pos"))
                playerArr.append(player)

        return playerArr


    def getTeamPlayers(self, teamName):

        teamArr = self.makeApiCall("https://api-nba-v1.p.rapidapi.com/teams", {"name":str(teamName)})
        
        if teamArr == False:
            return 0

        if len(teamArr.get("response")) == 0:
            return 1
        
        teamID = teamArr.get("response")[0].get("id")

        playerArr = self.makeApiCall("https://api-nba-v1.p.rapidapi.com/players", {"team":str(teamID),"season":"2021"})

        return self.getCurrentPlayers(playerArr.get("response"))

if __name__ == "__main__":
    t = TeamModel()
    t.getTeamPlayers("Toronto Raptors")

