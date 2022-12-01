import sys, os
import requests

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

class NewsApiCaller:

    def teamNewsApiCall(self, teamName):
        url = f"https://nba-latest-news.p.rapidapi.com/news/team/{teamName}"

        headers = {
            "X-RapidAPI-Key": "c5673b5906mshac24e0f63d333acp180e2bjsn8e180612cf71",
            "X-RapidAPI-Host": "nba-latest-news.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers)

        return response.text

    def allNewsApiCall(self):
        url = "https://nba-latest-news.p.rapidapi.com/news"

        headers = {
            "X-RapidAPI-Key": "c5673b5906mshac24e0f63d333acp180e2bjsn8e180612cf71",
            "X-RapidAPI-Host": "nba-latest-news.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        return response.text
