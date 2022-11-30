from prettytable import PrettyTable

class MainView:
    
       def getUserOption(self):
        print("Select an option by choosing a number:\n0. Exit program \n1. League Controller\n2. Search For A Team To See The Active Roster")
        option = input('->')

        while option != '1' and option != '0':
            print('Invalid selection. Please select an option choosing a number:\n0. Exit program \n1. League Controller\n2. Search For A Team To See The Active Roster')
            option = input('->')

        return option

    