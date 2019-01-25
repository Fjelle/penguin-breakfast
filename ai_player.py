import random

class Ai_player():
    def __init__(self,playernumber):
        self.name="Harry"
        self.behaviour=[1] #tells the ai what he should value
        self.priorities=[]
        self.money=5
        self.victory_points=0
        self.playernumber=playernumber

    def asktoinvest(self,companies_ingame):
        self.set_priorities(companies_ingame)
        print(self.priorities)

        for x in range(0,self.money):
            randomizes=random.uniform(0,1)
            print(randomizes)
            target_of_investment=0

            total=0
            subtotal=0
            for x in range(0,len(companies_ingame)):
                total+=self.priorities[x]
                if randomizes > subtotal  and randomizes < total:
                    target_of_investment=x
                subtotal=total

            companies_ingame[target_of_investment].ownership[self.playernumber]+=1

        for x in range(0,len(companies_ingame)):
            print(companies_ingame[x].ownership)


        self.money=0


    def set_priorities(self,companies_ingame):
        #set priorities
        self.priorities=[]
        for x in range(0,len(companies_ingame)):
            self.priorities.append(self.behaviour[0]*companies_ingame[x].return_value())

        #normalize priorities
        total=0
        for x in range(0,len(self.priorities)):
            total=total+self.priorities[x]
        for x in range(0,len(self.priorities)):
            self.priorities[x]=self.priorities[x]/total


    def reward_money(self,money):
        self.money+=money
    def reward_victory_points(self,victory_points):
        self.victory_points+=victory_points

    def recieve_message(self,message):
        message=message