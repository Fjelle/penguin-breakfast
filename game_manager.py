

class GameManager():


    def __init__(self, players, companies_ingame):
        self.players=players
        self.companies_ingame=companies_ingame

    def rewardphase(self): #checks which companies are owned by players and hands out rewards accordingly.
        for x in range(0,len(self.companies_ingame)):
            owner = self.companies_ingame[x].check_owner()
            if owner > -1 :
                if self.companies_ingame[x].return_type() == 1:
                    self.players[owner].reward_money(self.companies_ingame[x].return_value())
                else:
                    self.players[owner].reward_victory_points(self.companies_ingame[x].return_value())
                self.players[owner].recieve_message("You have been rewarded by company " + str(x+1)+"\n")

    def investmentphase(self): #asks the players to invest.
        for x in range(0,len(self.players)):
            self.players[x].asktoinvest(self.companies_ingame)
