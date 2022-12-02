import sys, os
import json
from prettytable import PrettyTable

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

class NewsModel:
    def __init__(self,ApiCaller):
        self.ApiCaller = ApiCaller
        self.allNews = []
        self.teamNews = []

    def pullAllNews(self):
        allNewsTable = PrettyTable()
        allNewsTable.field_names = ["Title", "URL", "Source"]
        allNewsTable.align = "l"
        allNewsTable.max_width= 100

        allNews = self.ApiCaller.newsApiCall('https://nba-latest-news.p.rapidapi.com/news')
        dictionary = json.loads(allNews)

        for news in dictionary:
            info = news['title'], news['url'], news['source']
            allNewsTable.add_row(info)

        self.allNews = allNewsTable

    def getAllNews(self):
        return self.allNews

    def pullTeamNews(self, teamName):
        teamNewsTable = PrettyTable()
        teamNewsTable.field_names = ["Title", "URL", "Source"]
        teamNewsTable.align = "l"
        teamNewsTable.max_width= 100
        
        teamNews = self.ApiCaller.newsApiCall(f"https://nba-latest-news.p.rapidapi.com/news/team/{teamName}")
        dictionary = json.loads(teamNews)

        for news in dictionary:
            info = news['title'], news['url'], news['source']
            teamNewsTable.add_row(info)

        self.teamNews = teamNewsTable

    def getTeamNews(self):
        return self.teamNews
