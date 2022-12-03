import sys, os
import json
from prettytable import PrettyTable

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

class NewsModel:
    
    # Constructor to call ApiCaller and create local variables allNews and teamNews
    def __init__(self,ApiCaller):
        self.ApiCaller = ApiCaller
        self.allNews = []
        self.teamNews = []

    # Method to pull all news using the newsAPI, and create a table using PrettyTable
    def pullAllNews(self):
        allNewsTable = PrettyTable()
        allNewsTable.field_names = ["Title", "URL", "Source"]
        allNewsTable.align = "l"
        allNewsTable.max_width= 100

        allNews = self.ApiCaller.newsApiCall('https://nba-latest-news.p.rapidapi.com/news')
        dictionary = json.loads(allNews)

        # Parse json response and add as rows to table
        for news in dictionary:
            info = news['title'], news['url'], news['source']
            allNewsTable.add_row(info)

        self.allNews = allNewsTable

    # Getter method to return allNews
    def getAllNews(self):
        return self.allNews

    # Method to pull news using the newsAPI when given a team name as a parameter, and create a table using PrettyTable
    def pullTeamNews(self, teamName):
        teamNewsTable = PrettyTable()
        teamNewsTable.field_names = ["Title", "URL", "Source"]
        teamNewsTable.align = "l"
        teamNewsTable.max_width= 100
        
        # Actual API call
        teamNews = self.ApiCaller.newsApiCall(f"https://nba-latest-news.p.rapidapi.com/news/team/{teamName}")
        dictionary = json.loads(teamNews)

        # Parse json response and as rows to table
        for news in dictionary:
            info = news['title'], news['url'], news['source']
            teamNewsTable.add_row(info)

        self.teamNews = teamNewsTable

    # Getter to return teamNews
    def getTeamNews(self):
        return self.teamNews
