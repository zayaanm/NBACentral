import sys, os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)
from View.NewsView import NewsView
from Model.NewsModel import NewsModel

class NewsController:
    def __init__(self,ApiCaller):
        self.NewsView = NewsView()
        self.NewsModel = NewsModel(ApiCaller)

    def showNews(self):
        newsPrompt = self.NewsView.getAllOrTeamPrompt()
        if (newsPrompt == '1'):
            self.NewsModel.pullAllNews()
            info = self.NewsModel.getAllNews()
            self.NewsView.displayAllNews(info)

        if(newsPrompt == '2'):
            teamName = self.NewsView.getTeamNamePrompt()
            self.NewsModel.pullTeamNews(teamName)
            info = self.NewsModel.getTeamNews()
            self.NewsView.displayTeamNews(teamName, info)

        if(newsPrompt == '3'):
            pass