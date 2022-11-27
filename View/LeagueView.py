from prettytable import PrettyTable

class LeagueView:

    def displayMainMenu(self):
        print('Please select an option:\n0.Go back to main menu\n1.Show league player stats\n2.Show conference stats')

        option = input('->')
        while option != '0' and option != '1' and option != '2':
            print('Invalid selection. Please select an option:\n0.Go back to main menu\n1.Show league player stats\n2.Show conference stats')
            option = input('->')

        return option

    def displayConferenceInfoPrompt(self):
        print("Select a year to get data for:\n1.2022\n2.2021\n3.2020\n4.2019\n5.2018\n6.2017\n7.2016\n8.2015")
        year = input('->')

        while year != '8' and year != '7' and year != '6' and year != '5' and year != '4' and year != '3' and year != '2' and year != '1':
            print('Invalid selection. Please select a year to get data for:\n1.2022\n2.2021\n3.2020\n4.2019\n5.2018\n6.2017\n7.2016\n8.2015')
            year = input('->')

        if year == '1':
            year = 2022
        elif year == '2':
            year = 2021
        elif year == '3':
            year = 2020
        elif year == '4':
            year = 2019
        elif year == '5':
            year = 2018
        elif year == '6':
            year = 2017
        elif year == '7':
            year = 2016
        elif year == '8':
            year = 2015

        print("Select a conference to get data for:\n1.Eastern\n2.Western")
        conference = input('->')

        while conference != '1' and conference != '2':
            print('Invalid selection. Please select a conference to get data for:\n1.Eastern\n2.Western')
            conference = input('->')

        if conference == '1':
            conference = 'east'
        elif conference == '2':
            conference = 'west'

        return year, conference

    def displayPlayerInfo(self,info):
        print('Here is the League Player info:\n' + info)

    def displayConferenceInfo(self,info):
        conferenceTable = PrettyTable()

        conferenceTable.field_names = ["Team Name", "Rank", "Wins", "Losses", "Win Percent"]
        
        for element in info:
            conferenceTable.add_row([element['fullName'], int(element['rank']), element['wins'], element['losses'], element['winPercent']])

        conferenceTable.sortby = 'Rank'

        print(conferenceTable)

    
    
