import random

class Ai_player():
    def __init__(self,playernumber, value_preference, rewarded_preference, behind_in_score_dislike, turn_count_modifier):

        self.behaviour=[value_preference,rewarded_preference, behind_in_score_dislike,turn_count_modifier] #tells the ai what he should value
        for x in range(0,len(self.behaviour)):
            if self.behaviour[x]<0:
                self.behaviour[x]=float(1/-self.behaviour[x])
            if self.behaviour[x]==0:
                self.behaviour[x]=1

        self.priorities=[]
        self.money=5
        self.victory_points=0
        self.playernumber=playernumber
        self.max_known_victory_points=0
        self.score=[]
        self.who_rewarded=[]
        self.turn_count=1

 #       self.preferences=[value_preference, rewarded_preference]

    def asktoinvest(self,companies_ingame):
        self.set_priorities(companies_ingame)

        for x in range(0,self.money):
            randomizes=random.uniform(0,1)
            target_of_investment=0

            total=0
            subtotal=0
            for x in range(0,len(companies_ingame)):
                total+=self.priorities[x]
                if randomizes > subtotal  and randomizes < total:
                    target_of_investment=x
                subtotal=total

            companies_ingame[target_of_investment].ownership[self.playernumber]+=1

        self.money=0


    def set_priorities(self,companies_ingame):
        #set priorities
        self.priorities=[]

        #sets up prioritization of valueable companies
        for x in range(0,len(companies_ingame)):
            self.priorities.append(companies_ingame[x].return_value()*self.behaviour[0])

        #sets up prioritization of victory points if player is behind proportional to how much player is behind
        if self.victory_points < max(self.score):
            for x in range(6,len(companies_ingame)):
                self.priorities[x]=self.priorities[x]*self.behaviour[2]*(max(self.score)-self.victory_points)

        #adjusts priorities based on whether the player owns the company
        for x in range(0,len(self.who_rewarded)):
            self.priorities[self.who_rewarded[x]]=self.priorities[self.who_rewarded[x]]*self.behaviour[1]
        self.who_rewarded=[]

        #priotitizes victory points later in the game.
        for x in range(6,len(companies_ingame)):
            self.priorities[x]=self.priorities[x]*self.turn_count*self.behaviour[3]
            self.turn_count+=1

        #normalize priorities.
        total=0
        for x in range(0,len(self.priorities)):
            total=total+self.priorities[x]
        for x in range(0,len(self.priorities)):
            self.priorities[x]=self.priorities[x]/total


    def reward_money(self,money):
        self.money+=money
    def reward_victory_points(self,victory_points):
        self.victory_points+=victory_points
    def return_victory_points(self):
        return self.victory_points
    def tell_score(self,score):
        self.score=score
    def tell_rewarded(self,company_number):
        self.who_rewarded.append(company_number)