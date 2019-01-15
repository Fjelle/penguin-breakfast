import player, company, game_manager


companies_setup=[1,1,1,2,2,3]   #these are the companies that can be invested in. Each entry in the list represents a company, the number represents the value of the company.
win_condition=30                #The game will end when a player owns 30 pounds or more.

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
    for x in range(0,len(companies_setup)):
        value=companies_setup[x]
        companies_ingame.append(company.Company(value,1,player_amount))

    #play until a player has earned enough money to win the game.
    manager=game_manager.GameManager(players,companies_ingame)
    most_money = 0
    while (most_money<win_condition):
        manager.investmentphase()
        manager.rewardphase()

        for x in range(0, len(players)):
            most_money = max(most_money, players[x].money)


    #check who won
    who_won = "player "
    for y in range(0,len(players)):
        if players[y].money == most_money:
            who_won=who_won+str(y+1)+" "
    who_won=who_won+"won the game."
    print(who_won)


main()
