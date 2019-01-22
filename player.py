import os

class Player():
    def __init__(self,playernumber):
        self.playernumber=playernumber
        self.victory_points=0
        self.money=5
        self.stored_message = '\n Company 1, 2 and 3 are worth 1 pound. \n Company 4 and 5 are worth 2 pounds. \n Company 6 is worth 3 pounds. \n \n company 7,8 and 9 are worth 1 victory point \n company 10 and 11 are worth 2 victory point\n company 12 is worth 3 victory points\n\n'

    def return_victory_points(self):
        return self.victory_points

    def recieve_message(self, message):
        self.stored_message=self.stored_message + message

    def print_message(self):
        print(self.stored_message)
        self.stored_message = '\n Company 1, 2 and 3 are worth 1. \n Company 4 and 5 are worth 2. \n Company 6 is worth 3. \n \n company 7,8 and 9 are worth 1 victory point \n company 10 and 11 are worth 2 victory point\n company 12 is worth 3 victory points\n\n'

    def return_money(self):
        return self.money

    def give_money(self,reward):
        self.money=self.money+reward

    def asktoinvest(self,companies_ingame):

        #clear the screen to that players do not see their opponents numbers.
        os.system('cls||clear')
        input("are you ready player " + str(self.playernumber +1)+"? \n")

        self.print_message()                            #print the information about the companies and rewards
        print("you currently have "+str(self.victory_points)+" victory point(s)\n")
        for x in range (0, len(companies_ingame)):      #ask the player to invest in the various companies
            company_number=x+1
            investment = -1
            while not (0 <= investment <= self.money):
                try:
                    investment = int(input("How much would you like to invest in company " + str(company_number)+ "? You have invested "+str(companies_ingame[x].return_investment(self.playernumber))+" in this company so far." +" You currently have " + str(self.money)+" pounds available to invest.\n"))

                    if investment > self.money:
                        print("You don't have that much money.")
                    elif investment < 0 :
                       print("that is silly.")

                except ValueError:
                    print("Please return a number.")
                    investment = -1

            self.money=self.money-int(investment)
            companies_ingame[x].ownership[self.playernumber]=companies_ingame[x].ownership[self.playernumber]+int(investment)

    def reward_money(self,reward_earned):
        self.money=self.money+reward_earned

    def reward_victory_points(self,reward_earned):
        self.victory_points=self.victory_points+reward_earned


