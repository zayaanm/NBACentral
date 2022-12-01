#Model For Player View
#Aidan David (251083708)

import json
import requests
import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

class PlayerModel:

    def __init__(self):
        pass

    def setPlayer(self, inp):
        pArray = self.APICall("https://api-nba-v1.p.rapidapi.com/players", {"name": str(inp[0]), "team": str(inp[1]), "season": "2021"})

        if pArray == False:
            return 0

        # if the player does not exist
        if len(pArray.get("response")) == 0:
            return 1

        playerIn = pArray.get("response")
        player = []
        pArray = []
        for x in playerIn:      #organizing information
            if x.get("nba").get("start") != 0 and "standard" in x.get("leagues") and x.get("leagues").get(
                    "standard").get("active") == True:
                player = []

                player.append(x.get("firstname"))
                player.append(x.get("lastname"))
                player.append(x.get("birth").get("date"))
                player.append(x.get("birth").get("country"))

                if x.get("height").get("feets") is not None and x.get("height").get("inches") is not None:
                    player.append(str(x.get("height").get("feets")) + "'" + str(x.get("height").get("inches")))
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
                pArray.append(player)

        return pArray

    def APICall(self, url, para):       #literally makes the API call

        headers = {
            "X-RapidAPI-Key": "bc1b759fdfmshb77a2031d4430cbp1169cfjsn62a876e90d2a",
            "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=para)

        if response.status_code != 200:
            return False

        pArray = json.loads(json.dumps(response.json()))

        return pArray