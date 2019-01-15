
class Player():
    def __init__(self,playernumber):
        self.playernumber=playernumber
        self.victory_points=0
        self.money=5

    def return_victory_points(self):
        return self.victory_points

    def return_money(self):
        return self.money
    def give_money(self,reward):
        self.money=self.money+reward

    def asktoinvest(self,companies_ingame):
        for x in range (0, len(companies_ingame)):
            company_number=x+1
            investment = -1
            while not (0 <= investment <= self.money):
                try:
                    investment = int(input("how much to invest in company " + str(company_number)+ ", you currently have " + str(self.money)+" available.\n"))
                except ValueError:
                    print("Please return a number.")
                    investment = -1

            self.money=self.money-int(investment)
            companies_ingame[x].ownership[self.playernumber]=companies_ingame[x].ownership[self.playernumber]+int(investment)


    def reward(self):
            print("a")


