import sys, os
import json
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from Helper.ApiCaller import ApiCaller

class NewsModel:
    def __init__(self,ApiCaller):
        self.ApiCaller = ApiCaller
        self.allNews = []
        self.teamNews = []

    def pullAllNews(self):
        allNews = self.ApiCaller.newsApiCall('https://nba-latest-news.p.rapidapi.com/news')
        allNews = json.loads(allNews)
        self.allNews = allNews
    
    def getAllNews(self):
        return self.allNews

    def pullTeamNews(self, teamName):
        teamNews = self.ApiCaller.newsApiCall(f"https://nba-latest-news.p.rapidapi.com/news/team/{teamName}")
        teamNews = json.loads(teamNews)
        # print(teamNews)
        self.teamNews = teamNews

    def getTeamNews(self):
        return self.teamNews