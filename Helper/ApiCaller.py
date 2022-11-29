import sys, os
import json
import requests

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

class ApiCaller:
    
    def __init__(self):
        config = ''
        with open("config.json", "r") as f:
            config = json.load(f)

        self.rapidApiKey = config["rapidApiKey"]["key"]
    
    def rapidApiCall(self, url):
        headers = {
            "X-RapidAPI-Key": self.rapidApiKey,
            "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        return response.text

        