from prettytable import PrettyTable

class NewsView:

    def getAllOrTeamPrompt(self):
        print("Select All News or Team News: \n1. All News\n2. Team News\n3. Return to Main Menu")
        userInput = input('->')

        return userInput

    def getTeamNamePrompt(self):
        print("Enter team name for which you want the news (Example, for Toronto Raptors, enter Raptors): ")
        userTeamInput = input('->')

        return userTeamInput.lower()

    def displayAllNews(self, news):
        print(news)


    def displayTeamNews(self, teamName, news):
        print(news)
