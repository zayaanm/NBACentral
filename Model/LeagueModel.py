import sys, os
import json
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

class LeagueModel:

    def __init__(self,ApiCaller):
        self.playerStats = 'player stats'
        self.conferenceStats = []
        self.apiCaller = ApiCaller

    def getConferenceStats(self):
        return self.conferenceStats

    def findConferenceStats(self,year,conference):
        teamStats = []
        teamNames = []
        appendedInfo = []

        standings = self.apiCaller.rapidApiCall(f'https://api-nba-v1.p.rapidapi.com/standings/standard/{year}/conference/{conference}')
        standings = json.loads(standings)

        for standing in standings['api']['standings']:
            info = dict(teamId = standing['teamId'], wins = standing['win'], losses = standing['loss'], rank = standing['conference']['rank'], winPercent = standing['winPercentage'])
            teamStats.append(info)

        
        teamInfo = self.apiCaller.rapidApiCall(f'https://api-nba-v1.p.rapidapi.com/teams/confName/{conference}')
        teamInfo = json.loads(teamInfo)

        for tinfo in teamInfo['api']['teams']:
            info = dict(teamId = tinfo['teamId'], fullName = tinfo['fullName'])
            teamNames.append(info)
        
        for ind, s in enumerate(teamStats):
            for sec, e in enumerate(teamNames):
                if s['teamId'] == e['teamId']:
                    appendedInfo.append(teamStats[ind] | teamNames[sec])
                    
        self.conferenceStats = appendedInfo

