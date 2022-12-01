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
        self.rapidApiKey2 = config["rapidApiKey2"]["key"]
        self.newsApiKey = config["newsApiKey"]["key"]
    
    def rapidApiCall(self, url):
        headers = {
            "X-RapidAPI-Key": self.rapidApiKey,
            "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        return response.text

    def rapidApiCalltoDict(self, url, parameters):

        #information for the api
        headers = {
            "X-RapidAPI-Key": self.rapidApiKey2,
            "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=parameters)

        #if api fails/cant be accessed
        if response.status_code != 200:
            return False

        #converting json file to a dictionary
        arr = json.loads(json.dumps(response.json()))

        return arr

    def newsApiCall(self, url):

        headers = {
            "X-RapidAPI-Key": self.newsApiKey,
            "X-RapidAPI-Host": "nba-latest-news.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        return response.text