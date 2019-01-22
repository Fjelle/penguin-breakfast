import player, company, game_manager


companies_setup_money=[1,1,1,2,2,3]     #these are the companies that will reward a player money when they invest in the company.
companies_setup_victory=[1,1,1,2,2,3]   #these are the companies that will reward victory points to the players.
win_condition=30                        #The game will end when a player owns 30 victory points or more.

def main():

    #allow the user to choose the amount of players in the game
    player_amount=-1
    while (player_amount == -1):
        try:
            player_amount=int(input("how many players will be playing?"))
            if player_amount<0:
                print("that is silly")
                player_amount=-1

        except ValueError:
            print("Please return a number.")
            player_amount = -1


    #set up players
    players=[]
    for x in range(0,player_amount):
        players.append(player.Player(x))

#    players=[player.Player(0),player.Player(1)]

    #set up a list containing the companies
    companies_ingame=[]
    for x in range(0,len(companies_setup_money)):
        value=companies_setup_money[x]
        companies_ingame.append(company.Company(value,1,player_amount))
    for z in range(0,len(companies_setup_victory)):
        value=companies_setup_victory[z]
        companies_ingame.append(company.Company(value,2,player_amount))

    #play until a player has earned enough money to win the game.
    manager=game_manager.GameManager(players,companies_ingame)
    most_victory_points = 0
    while (most_victory_points<win_condition):
        manager.investmentphase()
        manager.rewardphase()

        for x in range(0, len(players)):
            most_money = max(most_victory_points, players[x].money)


    #check who won
    who_won = "player "
    for y in range(0,len(players)):
        if players[y].money == most_victory_points:
            who_won=who_won+str(y+1)+" "
    who_won=who_won+"won the game."
    print(who_won)


main()
