import player, ai_player, company, game_manager, time, winsound


companies_setup_money=[1,1,1,2,2,3]     #these are the companies that will reward a player money when they invest in the company.
companies_setup_victory=[1,1,1,2,2,3]   #these are the companies that will reward victory points to the players.
win_condition=15                        #The game will end when a player owns 15 victory points or more.

iterations = 20
jumps = 50
games = 100

def main():
    start = time.time()

    recordofai=[] #used to store ai over various jumps
    player_amount=0
    ai_amount=2

    for iteration_counter in range(0,iterations):

        ai_file = open("ai2.txt", "r")
        ai2_behaviour = ai_file.readlines()
        for dd in range(0,len(ai2_behaviour)):
            ai2_behaviour[dd]=float(ai2_behaviour[dd])
        ai_file.close()




        for jumpcounter in range(1,jumps+1): #repeat for how many times the program should try to improve the ai

            win_array=[] #this list will contain how often the tested ai won against it's oppponent.

            jump_array=[-1,0,1]   #the ai's behaviour is tested around it's current value with this list.
            for gg in range(0,len(jump_array)):
                jump_array[gg]=jump_array[gg]*(1-jumpcounter/jumps)+0.1

            #here the ai tries 81 different behaviours surrounding the base behaviour.
            for ww in jump_array:
                for xx in jump_array:
                    for yy in jump_array:
                        for zz in jump_array:

                            ai_file = open("ai1.txt", "r")
                            ai1_behaviour = ai_file.readlines()
                            ai_file.close()

                            ai1_behaviour[0] = float(ai1_behaviour[0])+ ww
                            ai1_behaviour[1] = float(ai1_behaviour[1])+ xx
                            ai1_behaviour[2] = float(ai1_behaviour[2])+ yy
                            ai1_behaviour[3] = float(ai1_behaviour[3])+ zz


                            win_counter = 0

                            #and plays games with each of the 81 behaviours
                            for game_counter in range(0,games):

                                #allow the user to choose the amount of players in the game
                                #player_amount=-1
                                #ai_amount=-1

                                # while (player_amount == -1):
                                #     try:
                                #         player_amount=int(input("how many players will be playing?"))
                                #         if player_amount<0:
                                #             print("that is silly")
                                #             player_amount=-1
                                #         elif player_amount==0:
                                #             print("computers can have fun too")
                                #             break
                                #
                                #     except ValueError:
                                #         print("Please return a number.")
                                #         player_amount = -1
                                #
                                # while (ai_amount == -1):
                                #     try:
                                #         ai_amount=int(input("how many ai's will be playing?"))
                                #         if ai_amount<0:
                                #             print("that is silly")
                                #             ai_amount=-1
                                #         elif ai_amount==0:
                                #             print("no computers, fine")
                                #             break
                                #
                                #     except ValueError:
                                #         print("Please return a number.")
                                #         player_amount = -1


                                if  ai_amount == 0 and  player_amount ==0:
                                    print("no players and no AI's make for no game")
                                else:


                                    #set up players
                                    players=[]

                            #        for x in range(0,player_amount):
                            #            players.append(player.Player(x))


                                    players.append(ai_player.Ai_player(0+player_amount,float(ai1_behaviour[0]),float(ai1_behaviour[1]),float(ai1_behaviour[2]),float(ai1_behaviour[3])))
                                    players.append(ai_player.Ai_player(1 + player_amount, float(ai2_behaviour[0]), float(ai2_behaviour[1]),float(ai2_behaviour[2]), float(ai2_behaviour[3])))



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
                                            who_won=y
                                    who_won_string=who_won_string+"won the game.\n"
                                    print(who_won_string)

                                    if who_won == 0:
                                        win_counter += 1

                                    print("The final score was:\n")
                                    for x in range(0,len(players)):
                                        print("Player "+str(x+1)+" had "+str(players[x].victory_points)+" victory points.")

                            #here a record is made of the results of the games played and the behaviour involved
                            result_array=[win_counter, ai1_behaviour]
                            win_array.append(result_array)


            #the behaviour that scored best is taken as the new base behaviour to test around
            maxi=0
            winning_iteration=0
            for cc in range(0,len(win_array)):
                if win_array[cc][0] > maxi:
                    maxi=win_array[cc][0]
                    winning_iteration=cc


            ai1_behaviour=win_array[winning_iteration][1]
            recordofai.append(ai1_behaviour)



            #and is written in the ai file
            ai_file=open("ai1.txt","w")
            for qq in range(0,len(ai1_behaviour)):
                ai1_behaviour[qq]=str(ai1_behaviour[qq])
                ai_file.write(ai1_behaviour[qq]+"\n")
            ai_file.close()

            ai_file=open("ai_record.txt","a")
            for aa in range(0,len(ai1_behaviour)):
                ai_file.write(ai1_behaviour[aa]+"\n")
            ai_file.write(str(maxi/games)+"\n")
            ai_file.close()

        ai_file = open("ai2.txt", "w")
        for hh in range(0,len(ai1_behaviour)):
            ai_file.write(ai1_behaviour[hh]+"\n")
        ai_file.close()



    stop = time.time()
    print(stop-start)
    winsound.Beep(2500,500)


main()
