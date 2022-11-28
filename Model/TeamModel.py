import requests
import json


class TeamModel:

    teams = ["Atlanta Hawks",
             "Boston Celtics",
             "Brooklyn Nets",
             "Charlotte Hornets",
             "Chicago Bulls",
             "Cleveland Cavaliers",
             "Dallas Mavericks",
             "Denver Nuggets",
             "Detroit Pistons",
             "Golden State Warriors",
             "Houston Rockets",
             "Indiana Pacers",
             "Los Angeles Clippers",
             "Los Angeles Lakers",
             "Memphis Grizzlies",
             "Miami Heat",
             "Milwaukee Bucks",
             "Minnesota Timberwolves",
             "New Orleans Pelicans",
             "New York Knicks",
             "Oklahoma City Thunder",
             "Orlando Magic",
             "Philadelphia 76ers",
             "Phoenix Suns",
             "Portland Trail Blazers",
             "Sacramento Kings",
             "San Antonio Spurs",
             "Toronto Raptors",
             "Utah Jazz",
             "Washington Wizards"]
    
    def __init__(self):
        pass

    def makeApiCall(self, url, parameters):

        headers = {
            "X-RapidAPI-Key": "de229dde0cmsh61bafd93b3a54afp18db1djsn21ebcafe56ad",
            "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=parameters)

        if response.status_code != 200:
            return False

        arr = json.loads(json.dumps(response.json()))

        return arr

    def getCurrentPlayers(self, players):
        
        player = []
        playerArr = []
        for x in players:
            if x.get("nba").get("start") != 0 and "standard" in x.get("leagues") and x.get("leagues").get("standard").get("active") == True:
                player = []
                
                player.append(x.get("firstname"))
                player.append(x.get("lastname"))
                player.append(x.get("birth").get("date"))
                player.append(x.get("birth").get("country"))
                
                if x.get("height").get("feets") is not None and x.get("height").get("inches") is not None:
                    player.append(str(x.get("height").get("feets"))+"'"+str(x.get("height").get("inches")))
                else:
                    continue

                if x.get("weight").get("pounds") is not None:
                    player.append(str(x.get("weight").get("pounds")))
                else:
                    continue

                if x.get("leagues").get("standard").get("jersey") is not None:
                    player.append(x.get("leagues").get("standard").get("jersey"))
                else:
                    continue

                player.append(x.get("leagues").get("standard").get("pos"))
                playerArr.append(player)

        return playerArr


    def getTeamPlayers(self, teamName):

        playerArr = {'get': 'players/', 'parameters': {'team': '1', 'season': '2021'}, 'errors': [], 'results': 43, 'response': [{'id': 553, 'firstname': 'Lou', 'lastname': 'Williams', 'birth': {'date': '1986-10-27', 'country': 'USA'}, 'nba': {'start': 2005, 'pro': 16}, 'height': {'feets': '6', 'inches': '2', 'meters': '1.88'}, 'weight': {'pounds': '175', 'kilograms': '79.4'}, 'college': 'South Gwinnett HS (GA)', 'affiliation': 'South Gwinnett HS (GA)/USA', 'leagues': {'standard': {'jersey': 6, 'active': True, 'pos': 'G'}}}, {'id': 402, 'firstname': 'Jahlil', 'lastname': 'Okafor', 'birth': {'date': None, 'country': None}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': None, 'inches': None, 'meters': None}, 'weight': {'pounds': None, 'kilograms': None}, 'college': None, 'affiliation': None, 'leagues': {'standard': {'jersey': 14, 'active': False, 'pos': None}}}, {'id': 564, 'firstname': 'Delon', 'lastname': 'Wright', 'birth': {'date': '1992-04-26', 'country': 'USA'}, 'nba': {'start': 2015, 'pro': 6}, 'height': {'feets': '6', 'inches': '5', 'meters': '1.96'}, 'weight': {'pounds': '185', 'kilograms': '83.9'}, 'college': 'Utah', 'affiliation': 'Utah/USA', 'leagues': {'standard': {'jersey': 55, 'active': True, 'pos': 'G'}}}, {'id': 588, 'firstname': 'Cat', 'lastname': 'Barber', 'birth': {'date': '1994-07-25', 'country': 'USA'}, 'nba': {'start': 2021, 'pro': 0}, 'height': {'feets': None, 'inches': None, 'meters': None}, 'weight': {'pounds': None, 'kilograms': None}, 'college': 'North Carolina State', 'affiliation': 'North Carolina State/USA', 'leagues': {'standard': {'jersey': 5, 'active': False, 'pos': None}}}, {'id': 329, 'firstname': 'Timothe', 'lastname': 'Luwawu-Cabarrot', 'birth': {'date': '1995-05-09', 'country': 'France'}, 'nba': {'start': 2016, 'pro': 5}, 'height': {'feets': '6', 'inches': '7', 'meters': '2.01'}, 'weight': {'pounds': '215', 'kilograms': '97.5'}, 'college': 'Mega Basket', 'affiliation': 'Mega Basket/France', 'leagues': {'standard': {'jersey': 7, 'active': True, 'pos': 'G-F'}, 'africa': {'jersey': None, 'active': True, 'pos': 'G-F'}}}, {'id': 761, 'firstname': 'John', 'lastname': 'Collins', 'birth': {'date': '1997-09-23', 'country': 'USA'}, 'nba': {'start': 2017, 'pro': 4}, 'height': {'feets': '6', 'inches': '9', 'meters': '2.06'}, 'weight': {'pounds': '226', 'kilograms': '102.5'}, 'college': 'Wake Forest', 'affiliation': 'Wake Forest/USA', 'leagues': {'standard': {'jersey': 20, 'active': True, 'pos': 'F-C'}, 'africa': {'jersey': 20, 'active': True, 'pos': 'F-C'}, 'vegas': {'jersey': 20, 'active': True, 'pos': 'F-C'}, 'utah': {'jersey': 20, 'active': True, 'pos': 'F-C'}}}, {'id': 738, 'firstname': 'Jordan', 'lastname': 'Bell', 'birth': {'date': '1995-01-07', 'country': 'USA'}, 'nba': {'start': 2017, 'pro': 4}, 'height': {'feets': '6', 'inches': '7', 'meters': '2.01'}, 'weight': {'pounds': '216', 'kilograms': '98.0'}, 'college': 'Oregon', 'affiliation': 'Oregon/USA', 'leagues': {'standard': {'jersey': 20, 'active': True, 'pos': 'F'}, 'sacramento': {'jersey': 2, 'active': True, 'pos': 'F'}, 'vegas': {'jersey': 24, 'active': True, 'pos': 'F'}}}, {'id': 802, 'firstname': 'Wes', 'lastname': 'Iwundu', 'birth': {'date': '1994-12-20', 'country': 'USA'}, 'nba': {'start': 2017, 'pro': 0}, 'height': {'feets': None, 'inches': None, 'meters': None}, 'weight': {'pounds': None, 'kilograms': None}, 'college': 'Kansas State', 'affiliation': 'Kansas State/USA', 'leagues': {'standard': {'jersey': 4, 'active': True, 'pos': 'F'}, 'vegas': {'jersey': 25, 'active': True, 'pos': 'F'}}}, {'id': 1011, 'firstname': 'Cameron', 'lastname': 'Oliver', 'birth': {'date': '1996-07-11', 'country': 'USA'}, 'nba': {'start': 2020, 'pro': 1}, 'height': {'feets': '6', 'inches': '8', 'meters': '2.03'}, 'weight': {'pounds': '239', 'kilograms': '108.4'}, 'college': 'Nevada', 'affiliation': 'Nevada/USA', 'leagues': {'standard': {'jersey': 21, 'active': True, 'pos': 'F'}, 'vegas': {'jersey': 27, 'active': True, 'pos': 'F'}, 'sacramento': {'jersey': 27, 'active': True, 'pos': 'F'}}}, {'id': 980, 'firstname': 'Kevin', 'lastname': 'Huerter', 'birth': {'date': '1998-08-27', 'country': 'USA'}, 'nba': {'start': 2018, 'pro': 3}, 'height': {'feets': '6', 'inches': '7', 'meters': '2.01'}, 'weight': {'pounds': '198', 'kilograms': '89.8'}, 'college': 'Maryland', 'affiliation': 'Maryland/USA', 'leagues': {'standard': {'jersey': 9, 'active': True, 'pos': 'G-F'}, 'vegas': {'jersey': 1, 'active': True, 'pos': 'G'}, 'utah': {'jersey': 1, 'active': True, 'pos': 'G'}}}, {'id': 987, 'firstname': 'Kevin', 'lastname': 'Knox II', 'birth': {'date': '1999-08-11', 'country': 'USA'}, 'nba': {'start': 2018, 'pro': 3}, 'height': {'feets': '6', 'inches': '7', 'meters': '2.01'}, 'weight': {'pounds': '215', 'kilograms': '97.5'}, 'college': 'Kentucky', 'affiliation': 'Kentucky/USA', 'leagues': {'standard': {'jersey': 5, 'active': True, 'pos': 'F'}, 'vegas': {'jersey': 20, 'active': True, 'pos': 'F'}}}, {'id': 1046, 'firstname': 'Trae', 'lastname': 'Young', 'birth': {'date': '1998-09-19', 'country': 'USA'}, 'nba': {'start': 2018, 'pro': 3}, 'height': {'feets': '6', 'inches': '1', 'meters': '1.85'}, 'weight': {'pounds': '164', 'kilograms': '74.4'}, 'college': 'Oklahoma', 'affiliation': 'Oklahoma/USA', 'leagues': {'standard': {'jersey': 11, 'active': True, 'pos': 'G'}, 'vegas': {'jersey': 11, 'active': True, 'pos': 'G'}, 'utah': {'jersey': 11, 'active': True, 'pos': 'G'}}}, {'id': 977, 'firstname': 'Johnny', 'lastname': 'Hamilton', 'birth': {'date': None, 'country': None}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': None, 'inches': None, 'meters': None}, 'weight': {'pounds': None, 'kilograms': None}, 'college': None, 'affiliation': None, 'leagues': {'standard': {'jersey': 24, 'active': False, 'pos': None}, 'vegas': {'jersey': 49, 'active': True, 'pos': 'C'}}}, {'id': 923, 'firstname': 'DeVaughn', 'lastname': 'Akoon-Purcell', 'birth': {'date': None, 'country': None}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': None, 'inches': None, 'meters': None}, 'weight': {'pounds': None, 'kilograms': None}, 'college': None, 'affiliation': None, 'leagues': {'standard': {'jersey': 44, 'active': False, 'pos': None}, 'vegas': {'jersey': 42, 'active': True, 'pos': 'F'}}}, {'id': 2211, 'firstname': 'Justin', 'lastname': 'Tillman', 'birth': {'date': None, 'country': None}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': None, 'inches': None, 'meters': None}, 'weight': {'pounds': None, 'kilograms': None}, 'college': None, 'affiliation': None, 'leagues': {'vegas': {'jersey': 64, 'active': True, 'pos': 'F'}, 'standard': {'jersey': None, 'active': True, 'pos': 'F'}}}, {'id': 2165, 'firstname': 'Chris', 'lastname': 'Clemons', 'birth': {'date': None, 'country': None}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': None, 'inches': None, 'meters': None}, 'weight': {'pounds': None, 'kilograms': None}, 'college': None, 'affiliation': None, 'leagues': {'vegas': {'jersey': 39, 'active': True, 'pos': 'G'}, 'standard': {'jersey': 39, 'active': False, 'pos': None}}}, {'id': 2579, 'firstname': 'Javin', 'lastname': 'DeLaurier', 'birth': {'date': '1998-04-07', 'country': 'USA'}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': '6', 'inches': '10', 'meters': '2.08'}, 'weight': {'pounds': '234', 'kilograms': '106.1'}, 'college': 'Duke', 'affiliation': 'Duke/USA', 'leagues': {'standard': {'jersey': 12, 'active': True, 'pos': 'C'}, 'vegas': {'jersey': 40, 'active': True, 'pos': 'F-C'}}}, {'id': 1948, 'firstname': 'DaQuan', 'lastname': 'Jeffries', 'birth': {'date': '1997-08-30', 'country': 'USA'}, 'nba': {'start': 2019, 'pro': 3}, 'height': {'feets': '6', 'inches': '5', 'meters': '1.96'}, 'weight': {'pounds': '225', 'kilograms': '102.1'}, 'college': 'Tulsa', 'affiliation': 'Tulsa/USA', 'leagues': {'vegas': {'jersey': 16, 'active': True, 'pos': 'F'}, 'standard': {'jersey': 8, 'active': True, 'pos': 'G-F'}, 'utah': {'jersey': 55, 'active': True, 'pos': 'G-F'}}}, {'id': 1889, 'firstname': 'Cam', 'lastname': 'Reddish', 'birth': {'date': '1999-09-01', 'country': 'USA'}, 'nba': {'start': 2019, 'pro': 2}, 'height': {'feets': '6', 'inches': '8', 'meters': '2.03'}, 'weight': {'pounds': '217', 'kilograms': '98.4'}, 'college': 'Duke', 'affiliation': 'Duke/USA', 'leagues': {'standard': {'jersey': None, 'active': True, 'pos': 'F-G'}}}, {'id': 1868, 'firstname': "De'Andre", 'lastname': 'Hunter', 'birth': {'date': '1997-12-02', 'country': 'USA'}, 'nba': {'start': 2019, 'pro': 2}, 'height': {'feets': '6', 'inches': '8', 'meters': '2.03'}, 'weight': {'pounds': '221', 'kilograms': '100.2'}, 'college': 'Virginia', 'affiliation': 'Virginia/USA', 'leagues': {'standard': {'jersey': 12, 'active': True, 'pos': 'F-G'}, 'vegas': {'jersey': 12, 'active': True, 'pos': 'F'}}}, {'id': 1892, 'firstname': 'Admiral', 'lastname': 'Schofield', 'birth': {'date': '1997-03-30', 'country': 'United Kingdom'}, 'nba': {'start': 2019, 'pro': 1}, 'height': {'feets': '6', 'inches': '5', 'meters': '1.96'}, 'weight': {'pounds': '241', 'kilograms': '109.3'}, 'college': 'Tennessee', 'affiliation': 'Tennessee/United Kingdom', 'leagues': {'standard': {'jersey': 25, 'active': True, 'pos': 'F'}, 'vegas': {'jersey': 25, 'active': True, 'pos': 'F'}}}, {'id': 2388, 'firstname': 'Jeremiah', 'lastname': 'Martin', 'birth': {'date': '1996-06-19', 'country': 'USA'}, 'nba': {'start': 2019, 'pro': 2}, 'height': {'feets': '6', 'inches': '2', 'meters': '1.88'}, 'weight': {'pounds': '185', 'kilograms': '83.9'}, 'college': 'Memphis', 'affiliation': 'Memphis/USA', 'leagues': {'standard': {'jersey': 3, 'active': True, 'pos': 'G'}, 'vegas': {'jersey': 10, 'active': True, 'pos': 'G'}}}, {'id': 2629, 'firstname': 'Onyeka', 'lastname': 'Okongwu', 'birth': {'date': '2000-12-11', 'country': 'USA'}, 'nba': {'start': 2020, 'pro': 1}, 'height': {'feets': '6', 'inches': '8', 'meters': '2.03'}, 'weight': {'pounds': '240', 'kilograms': '108.9'}, 'college': 'Southern California', 'affiliation': 'Southern California/USA', 'leagues': {'standard': {'jersey': 17, 'active': True, 'pos': 'F-C'}}}, {'id': 2620, 'firstname': 'Skylar', 'lastname': 'Mays', 'birth': {'date': '1997-09-05', 'country': 'USA'}, 'nba': {'start': 2020, 'pro': 1}, 'height': {'feets': '6', 'inches': '4', 'meters': '1.93'}, 'weight': {'pounds': '205', 'kilograms': '93.0'}, 'college': 'Louisiana State', 'affiliation': 'Louisiana State/USA', 'leagues': {'standard': {'jersey': 4, 'active': True, 'pos': 'G'}, 'vegas': {'jersey': 4, 'active': True, 'pos': 'G'}}}, {'id': 2979, 'firstname': 'Nahziah', 'lastname': 'Carter', 'birth': {'date': '1999-08-24', 'country': 'USA'}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': '6', 'inches': '6', 'meters': '1.98'}, 'weight': {'pounds': '205', 'kilograms': '93.0'}, 'college': 'Washington', 'affiliation': 'Washington/USA', 'leagues': {'vegas': {'jersey': 31, 'active': True, 'pos': 'G'}}}, {'id': 2800, 'firstname': 'Sharife', 'lastname': 'Cooper', 'birth': {'date': '2001-06-11', 'country': 'USA'}, 'nba': {'start': 2021, 'pro': 0}, 'height': {'feets': '6', 'inches': '1', 'meters': '1.85'}, 'weight': {'pounds': '176', 'kilograms': '79.8'}, 'college': 'Auburn', 'affiliation': 'Auburn/USA', 'leagues': {'standard': {'jersey': 2, 'active': True, 'pos': 'G'}, 'vegas': {'jersey': 2, 'active': True, 'pos': 'G'}}}, {'id': 2819, 'firstname': 'Jalen', 'lastname': 'Johnson', 'birth': {'date': '2001-12-18', 'country': 'USA'}, 'nba': {'start': 2021, 'pro': 0}, 'height': {'feets': '6', 'inches': '8', 'meters': '2.03'}, 'weight': {'pounds': '219', 'kilograms': '99.3'}, 'college': 'Duke', 'affiliation': 'Duke/USA', 'leagues': {'standard': {'jersey': 1, 'active': True, 'pos': 'F'}, 'vegas': {'jersey': 1, 'active': True, 'pos': 'F'}}}, {'id': 2794, 'firstname': 'Chaundee', 'lastname': 'Brown Jr.', 'birth': {'date': '1998-12-04', 'country': 'USA'}, 'nba': {'start': 2021, 'pro': 0}, 'height': {'feets': '6', 'inches': '5', 'meters': '1.96'}, 'weight': {'pounds': '215', 'kilograms': '97.5'}, 'college': 'Michigan', 'affiliation': 'Michigan/USA', 'leagues': {'standard': {'jersey': 38, 'active': True, 'pos': 'F'}, 'sacramento': {'jersey': 15, 'active': True, 'pos': 'G'}, 'vegas': {'jersey': 45, 'active': True, 'pos': 'G'}}}, {'id': 2890, 'firstname': 'A.J.', 'lastname': 'Lawson', 'birth': {'date': '2000-07-15', 'country': 'Canada'}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': '6', 'inches': '6', 'meters': '1.98'}, 'weight': {'pounds': '180', 'kilograms': '81.6'}, 'college': 'South Carolina', 'affiliation': 'South Carolina/Canada', 'leagues': {'sacramento': {'jersey': 58, 'active': True, 'pos': 'G'}, 'vegas': {'jersey': 29, 'active': True, 'pos': 'G'}, 'standard': {'jersey': 5, 'active': True, 'pos': 'G'}}}, {'id': 3395, 'firstname': 'Malik', 'lastname': 'Ellison', 'birth': {'date': None, 'country': None}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': None, 'inches': None, 'meters': None}, 'weight': {'pounds': None, 'kilograms': None}, 'college': None, 'affiliation': None, 'leagues': {'standard': {'jersey': None, 'active': True, 'pos': 'G'}, 'vegas': {'jersey': 28, 'active': True, 'pos': 'G'}, 'utah': {'jersey': 28, 'active': True, 'pos': 'G'}}}, {'id': 3380, 'firstname': 'Malcolm', 'lastname': 'Hill', 'birth': {'date': '1995-10-26', 'country': 'USA'}, 'nba': {'start': 2021, 'pro': 0}, 'height': {'feets': '6', 'inches': '6', 'meters': '1.98'}, 'weight': {'pounds': '220', 'kilograms': '99.8'}, 'college': 'Illinois', 'affiliation': 'Illinois/USA', 'leagues': {'standard': {'jersey': 14, 'active': True, 'pos': 'F'}, 'vegas': {'jersey': 21, 'active': True, 'pos': 'G-F'}}}, {'id': 3382, 'firstname': 'Ibi', 'lastname': 'Watson-Boye', 'birth': {'date': None, 'country': None}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': None, 'inches': None, 'meters': None}, 'weight': {'pounds': None, 'kilograms': None}, 'college': None, 'affiliation': None, 'leagues': {'standard': {'jersey': 16, 'active': False, 'pos': None}}}, {'id': 181, 'firstname': 'Danilo', 'lastname': 'Gallinari', 'birth': {'date': '1988-08-08', 'country': 'Italy'}, 'nba': {'start': 2008, 'pro': 12}, 'height': {'feets': '6', 'inches': '10', 'meters': '2.08'}, 'weight': {'pounds': '236', 'kilograms': '107.0'}, 'college': 'Olimpia Milano', 'affiliation': 'Olimpia Milano/Italy', 'leagues': {'standard': {'jersey': 8, 'active': True, 'pos': 'F'}, 'africa': {'jersey': 8, 'active': True, 'pos': 'F'}}}, {'id': 497, 'firstname': 'Lance', 'lastname': 'Stephenson', 'birth': {'date': '1990-09-05', 'country': 'USA'}, 'nba': {'start': 2010, 'pro': 9}, 'height': {'feets': '6', 'inches': '5', 'meters': '1.96'}, 'weight': {'pounds': '210', 'kilograms': '95.3'}, 'college': 'Cincinnati', 'affiliation': 'Cincinnati/USA', 'leagues': {'standard': {'jersey': 6, 'active': True, 'pos': 'F'}}}, {'id': 141, 'firstname': 'Gorgui', 'lastname': 'Dieng', 'birth': {'date': '1990-01-18', 'country': 'Senegal'}, 'nba': {'start': 2013, 'pro': 8}, 'height': {'feets': '6', 'inches': '10', 'meters': '2.08'}, 'weight': {'pounds': '248', 'kilograms': '112.5'}, 'college': 'Louisville', 'affiliation': 'Louisville/Senegal', 'leagues': {'standard': {'jersey': 10, 'active': True, 'pos': 'C'}}}, {'id': 239, 'firstname': 'Solomon', 'lastname': 'Hill', 'birth': {'date': '1991-03-18', 'country': 'USA'}, 'nba': {'start': 2013, 'pro': 0}, 'height': {'feets': None, 'inches': None, 'meters': None}, 'weight': {'pounds': None, 'kilograms': None}, 'college': 'Arizona', 'affiliation': 'Arizona/USA', 'leagues': {'standard': {'jersey': 99, 'active': False, 'pos': None}}}, {'id': 372, 'firstname': 'Eric', 'lastname': 'Moreland', 'birth': {'date': None, 'country': None}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': None, 'inches': None, 'meters': None}, 'weight': {'pounds': None, 'kilograms': None}, 'college': None, 'affiliation': None, 'leagues': {'standard': {'jersey': 25, 'active': False, 'pos': None}, 'vegas': {'jersey': 25, 'active': True, 'pos': 'F'}}}, {'id': 92, 'firstname': 'Clint', 'lastname': 'Capela', 'birth': {'date': '1994-05-18', 'country': 'Switzerland'}, 'nba': {'start': 2014, 'pro': 7}, 'height': {'feets': '6', 'inches': '10', 'meters': '2.08'}, 'weight': {'pounds': '256', 'kilograms': '116.1'}, 'college': 'Elan Chalon', 'affiliation': 'Elan Chalon/Switzerland', 'leagues': {'standard': {'jersey': 15, 'active': True, 'pos': 'C'}}}, {'id': 743, 'firstname': 'Bogdan', 'lastname': 'Bogdanovic', 'birth': {'date': '1992-08-18', 'country': 'Serbia'}, 'nba': {'start': 2017, 'pro': 4}, 'height': {'feets': '6', 'inches': '6', 'meters': '1.98'}, 'weight': {'pounds': '225', 'kilograms': '102.1'}, 'college': 'Fenerbahce', 'affiliation': 'Fenerbahce/Serbia', 'leagues': {'standard': {'jersey': 13, 'active': True, 'pos': 'G'}}}, {'id': 3006, 'firstname': 'Juwan', 'lastname': 'Durham', 'birth': {'date': '1997-12-22', 'country': None}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': '6', 'inches': '11', 'meters': '2.11'}, 'weight': {'pounds': '231', 'kilograms': '104.8'}, 'college': 'Notre Dame', 'affiliation': None, 'leagues': {'vegas': {'jersey': 30, 'active': True, 'pos': 'F'}}}, {'id': 3057, 'firstname': 'Max', 'lastname': 'Heidegger', 'birth': {'date': '1997-06-05', 'country': 'USA'}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': '6', 'inches': '3', 'meters': '1.9'}, 'weight': {'pounds': '180', 'kilograms': '81.6'}, 'college': 'California-Santa Barbara', 'affiliation': 'California-Santa Barbara/USA', 'leagues': {'vegas': {'jersey': 26, 'active': True, 'pos': 'G'}}}, {'id': 3072, 'firstname': 'Justin', 'lastname': 'Jaworski', 'birth': {'date': '1999-06-21', 'country': None}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': '6', 'inches': '3', 'meters': '1.9'}, 'weight': {'pounds': '196', 'kilograms': '88.9'}, 'college': 'Lafayette', 'affiliation': None, 'leagues': {'vegas': {'jersey': 33, 'active': True, 'pos': 'G'}}}, {'id': 3263, 'firstname': 'Ibi', 'lastname': 'Watson', 'birth': {'date': '1998-01-06', 'country': None}, 'nba': {'start': 0, 'pro': 0}, 'height': {'feets': '6', 'inches': '5', 'meters': '1.96'}, 'weight': {'pounds': '200', 'kilograms': '90.7'}, 'college': 'Dayton', 'affiliation': None, 'leagues': {'vegas': {'jersey': 16, 'active': True, 'pos': 'G'}}}]}

        #teamArr = self.makeApiCall("https://api-nba-v1.p.rapidapi.com/teams", {"name":str(teamName)})
        
        #if teamArr == False:
        #    return 0

        #if len(teamArr.get("response")) == 0:
        #    return 1
        
        #teamID = teamArr.get("response")[0].get("id")

        #playerArr = self.makeApiCall("https://api-nba-v1.p.rapidapi.com/players", {"team":str(teamID),"season":"2021"}, )
        #print(playerArr)

        #print("-----------------------------------------------")

        #print(arr.get("response")[0].get("firstname"))

        print(self.getCurrentPlayers(playerArr.get("response")))

        return self.getCurrentPlayers(playerArr.get("response"))

if __name__ == "__main__":
    t = TeamModel()
    t.getTeamPlayers("Toronto Raptors")

