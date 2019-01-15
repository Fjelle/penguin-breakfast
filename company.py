
class Company():
    def __init__(self, value, type):
        self.value=value
        self.type=type
        self.ownership=[0,0]

    def return_value(self):
        return self.value

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
