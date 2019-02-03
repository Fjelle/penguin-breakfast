import player, ai_player, company, game_manager, time, winsound


companies_setup_money=[1,1,1,2,2,3]     #these are the companies that will reward a player money when they invest in the company.
companies_setup_victory=[1,1,1,2,2,3]   #these are the companies that will reward victory points to the players.
win_condition=15                        #The game will end when a player owns 15 victory points or more.

def main():

    #allow the user to choose the amount of players in the game
    player_amount=-1
    ai_amount=-1

    while (player_amount == -1):
        try:
            player_amount=int(input("how many players will be playing?"))
            if player_amount<0:
                print("that is silly")
                player_amount=-1
            elif player_amount==0:
                print("computers can have fun too")
                break

        except ValueError:
            print("Please return a number.")
            player_amount = -1

    while (ai_amount == -1):
        try:
            ai_amount=int(input("how many ai's will be playing?"))
            if ai_amount<0:
                print("that is silly")
                ai_amount=-1
            elif ai_amount==0:
                print("no computers, fine")
                break

        except ValueError:
            print("Please return a number.")
            player_amount = -1


        if  ai_amount == 0 and  player_amount ==0:
            print("no players and no AI's make for no game")
        else:


            #set up players
           players=[]

           for x in range(0,player_amount):
               players.append(player.Player(x))

           for y in range(0,ai_amount):
               players.append(ai_player.Ai_player(player_amount+y,1,1,1,1))



           #set up a list containing the companies
           companies_ingame=[]
           for x in range(0,len(companies_setup_money)):
               value=companies_setup_money[x]
               companies_ingame.append(company.Company(value,1,player_amount+ai_amount))
           for z in range(0,len(companies_setup_victory)):
               value=companies_setup_victory[z]
               companies_ingame.append(company.Company(value,2,player_amount+ai_amount))

           #play until a player has earned enough money to win the game.
           turn_counter=0
           manager=game_manager.GameManager(players,companies_ingame)
           most_victory_points = 0
           while (most_victory_points<win_condition) and turn_counter<=100:
               manager.investmentphase()
               manager.rewardphase()
               turn_counter+=1
               for x in range(0, len(players)):
                   most_victory_points = max(most_victory_points, players[x].victory_points)



           #check who won
           who_won_string = "\nPlayer "
           for y in range(0,len(players)):
               if players[y].victory_points == most_victory_points:
                   who_won_string=who_won_string+str(y+1)+" "
           who_won_string=who_won_string+"won the game.\n"
           print(who_won_string)




main()
