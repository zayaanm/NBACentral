from prettytable import PrettyTable

class NewsView:

    # Method to ask for user input on whether they want to see all news or team news.
    # Returns user response 
    def getAllOrTeamPrompt(self):
        print("Select All News or Team News: \n1. All News\n2. Team News\n3. Return to Main Menu")
        userInput = input('->')

        return userInput

    # Method to ask user for team name. Converts user response to lowercase.
    def getTeamNamePrompt(self):
        print("Enter team name for which you want the news (Example, for Toronto Raptors, enter Raptors): ")
        userTeamInput = input('->')

        return userTeamInput.lower()

    # Method to print allNewstable being passed from newsModel
    def displayAllNews(self, news):
        print(news)

    # Method to print teamNewsModel being passed from newsModel
    def displayTeamNews(self, news):
        print(news)
