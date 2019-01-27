

class GameManager():


    def __init__(self, players, companies_ingame):
        self.players=players
        self.companies_ingame=companies_ingame
        self_company_ownership=[]

    def rewardphase(self): #checks which companies are owned by players and hands out rewards accordingly.
        self.company_ownership=[]
        for x in range(0,len(self.companies_ingame)):
            owner = self.companies_ingame[x].check_owner()
            self.company_ownership.append(owner)
            if owner > -1 :
                self.players[owner].tell_rewarded(x)
                if self.companies_ingame[x].return_type() == 1: #this company is a money company
                    self.players[owner].reward_money(self.companies_ingame[x].return_value())
                else:                                           #or it is a victory company
                    self.players[owner].reward_victory_points(self.companies_ingame[x].return_value())




    def investmentphase(self): #asks the players to invest.

        score=[]  #prepares the scores to be send to the players
        for z in range(0,len(self.players)):
            score.append(self.players[z].return_victory_points())

        for x in range(0,len(self.players)): #players are told the scores and asked to invest
            self.players[x].tell_score(score)
            self.players[x].asktoinvest(self.companies_ingame)
