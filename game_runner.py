import player, company

companies_setup=[1,1,1,2,2,3]

def main():
    #set up two players
    players=[player.Player(0),player.Player(1)]

    #set up a list containing the companies
    companies_ingame=[]
    for x in range(0,len(companies_setup)):
        value=companies_setup[x]
        companies_ingame.append(company.Company(value,1))

    #play until a player has earned enough money to win the game.
    while (players[0].return_money()<=30) and (players[1].return_money()<= 30):
        players[0].asktoinvest(companies_ingame)
        players[1].asktoinvest(companies_ingame)

    #check who won
    if players[0].return_money()>players[1].return_money():
        print("player one won")
    elif players[0].return_money()<players[1].return_money():
        print("player two won")
    else:
        print("it is a tie!")


main()
