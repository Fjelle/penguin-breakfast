# penguin-breakfast
Framework to play the game of 'penguins'. Developed primarily to play test the game, but also to have a go at developing an AI later on.

The goal of the game is to earn victory points. The game ends when a player owns more victory points than the set goal. The player with the most victory points at that point wins the game. Victory points are earned by investing in certain companies. Other companies may reward a player money that can be re-invested later in the game. 

This game is played in two repeating phases. In phase one the players get to invest their money in several companies. Players know how much they invested in a company, but have little information as to what investments their opponent(s) made. Phase two is the reward phase. Each company has a value and a type. The first type of company rewards it's biggest investor money, a second type of company rewards it's biggest investor victory points. On a tie, no reward is given. Player are told which companies rewarded them, but not which companies rewarded their opponent(s) or which companies did not reward any player. After the reward phase, the game returns to the investment phase and the players are asked to invest their newly earned money. 

Current status:

   master branch: this branch is used to develop the AI. The AI tests it's behaviour against itself and other AI players and improves it's behaviour based on the results. The expectation was that the AI would reach a steady state (or Nash equilibrium) by iterating the script for a long time, but that does not seem to be the case. The next step is to figure out whether that is because of a fault in the code or because of the nature of the game.
    
   Playable: this branch allows the user to play 'penguins' against any number of friends and/or AI. The AI is currently trained to play against a single opponent.

Things to do: improve AI, publish game on website. 

