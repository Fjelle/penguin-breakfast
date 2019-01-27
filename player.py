import os

class Player():
    def __init__(self,playernumber):
        self.score=[]
        self.rewarded_by=[]
        self.playernumber=playernumber
        self.victory_points=0
        self.money=5

    def return_victory_points(self):
        return self.victory_points

    def tell_rewarded(self,company_number):
        self.rewarded_by.append(company_number)

    def tell_score(self,score):
        self.score=score

    def return_money(self):
        return self.money

    def give_money(self,reward):
        self.money=self.money+reward

    def asktoinvest(self,companies_ingame):

        #clear the screen to that players do not see their opponents numbers.
        os.system('cls||clear')
        input("are you ready player " + str(self.playernumber +1)+"? \n")

        #give the player the necessary information about the game
        print('\n Company 1, 2 and 3 are worth 1 pound. \n Company 4 and 5 are worth 2 pounds. \n Company 6 is worth 3 pounds. \n \n company 7,8 and 9 are worth 1 victory point \n company 10 and 11 are worth 2 victory point\n company 12 is worth 3 victory points\n')

        for x in range(0,len(self.score)):
            print("Player " + str(x + 1) + " has " + str(self.score[x]) + " victory points")
        print("\n")

        for x in range(0,len(self.rewarded_by)):
            print("you have been rewarded by company "+str(self.rewarded_by[x]+1))
        print("\n")
        self.rewarded_by=[]

        #ask the player to invest in the various companies
        for x in range (0, len(companies_ingame)):
            company_number=x+1
            investment = -1
            while not (0 <= investment <= self.money):
                try:
                    investment = int(input("How much would you like to invest in company " + str(company_number)+ "? You have invested "+str(companies_ingame[x].return_investment(self.playernumber))+" in this company so far." +" You currently have " + str(self.money)+" pounds available to invest.\n"))

                    if investment > self.money:
                        print("You don't have that much money.")
                    elif investment == -3:

                        break
                    elif investment < 0 :
                       print("that is silly.")

                except ValueError:
                    print("Please return a number.")
                    investment = -1

            if investment == -3: #allows to quickly skip a player by entering -3 for an investment
                break

            self.money=self.money-int(investment)
            companies_ingame[x].ownership[self.playernumber]=companies_ingame[x].ownership[self.playernumber]+int(investment)

    def reward_money(self,reward_earned):
        self.money=self.money+reward_earned

    def reward_victory_points(self,reward_earned):
        self.victory_points=self.victory_points+reward_earned


