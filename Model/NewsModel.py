import sys, os
import json
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

from Helper.NewsApiCaller import NewsApiCaller

class NewsModel:
    def __init__(self):
        self.newsApiCaller = NewsApiCaller()
        self.allNews = []
        self.teamNews = []

    def pullAllNews(self):
        allNews = self.newsApiCaller.allNewsApiCall()
        allNews = json.loads(allNews)
        # print(allNews)
        self.allNews = allNews
    
    def getAllNews(self):
        return self.allNews

    def pullTeamNews(self, teamName):
        teamNews = self.newsApiCaller.teamNewsApiCall(teamName)
        teamNews = json.loads(teamNews)
        # print(teamNews)
        self.teamNews = teamNews

    def getTeamNews(self):
        return self.teamNews