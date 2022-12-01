class MainView:
    
       def getUserOption(self):
        print("Select an option by choosing a number:\n0. Exit program \n1. Get conference standings\n2. Search for team roster\n3. See news\n4. Get player stats")
        option = input('->')

        while  option != '4' and option != '3' and option != '2' and option != '1' and option != '0':
            print('Invalid selection. Please select an option choosing a number:\n0. Exit program \n1. Get conference standings\n2. Search for team roster\n3. See news\n4. Get player stats')
            option = input('->')

        return option

    