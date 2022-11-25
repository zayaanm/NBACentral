class LeagueView:

    def displayMainMenu(self):
        option = input('Please select an option:\n0.Go back to main menu\n1.Show league player stats\n2.Show conference stats\n')

        while option != '0' and option != '1' and option != '2':
            option = input('Invalid selection. Please select an option:\n0.Go back to main menu\n1.Show league player stats\n2.Show conference stats\n')

        return option

    def displayPlayerInfo(self,info):
        print('Here is the League Player info:\n' + info)

    def displayConferenceInfo(self,info):
        print('Here is the League Conference info:\n' + info)

    
    
