#Model For Player View
#Aidan David (251083708)

class PlayerModel:

    def setPlayer(self, pName):
        found = True

        #api call name
        if(1 == 1):  #this is going to be a flip for when api call is successful
            found = True

        if(found == False):
            return False

        self.name = 'y'
        self.pos = "y"
        self.age = "y"
        self.team = "y"
        self.num = "y"
        self.hgt = "y"
        self.pts = "y"
        self.ats = "y"
        self.stls = "y"
        self.rbs = "y"
        self.blks = "y"
        self.tos = "y"
        self.pm = "y"

        return True

    def getName(self):
        return self.name

    def getPosition(self):
        return self.pos

    def getAge(self):
        return self.age

    def getTeam(self):
        return self.team

    def getNumber(self):
        return self.num

    def getHeight(self):
        return self.hgt

    def getPoints(self):
        return self.pts

    def getAssists(self):
        return self.ats

    def getSteals(self):
        return self.stls

    def getRebounds(self):
        return self.rbs

    def getBlocks(self):
        return self.blks

    def getTurnOvers(self):
        return self.tos

    def getPlusMinus(self):
        return self.pm