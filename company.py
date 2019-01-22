
class Company():
    def __init__(self, value, type, player_amount):
        self.value=value        #how much to players earn when they control this company
        self.type=type          #indicates whether comany rewards players with money or victory points, 1=money, 2=victory points

        self.ownership=[]    #records investments made by players.
        for x in range(0,player_amount):
            self.ownership.append(0)

    def return_value(self):
        return self.value
    def return_type(self):
        return self.type
    def return_investment(self,playernumber):
        return self.ownership[playernumber]

    def check_owner(self): #returns the player who owns the company, returns -1 in case of a tie
        winningplayer = 0
        maxinvestment = self.ownership[0]
        for x in range(1,len(self.ownership)):
            if self.ownership[x] > maxinvestment:
                maxinvestment = self.ownership[x]
                winningplayer = x
            elif self.ownership[x] == maxinvestment:
                winningplayer = -1

        return winningplayer


