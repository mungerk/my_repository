'''
Katy Munger and Andrew Fitch
1/22/2018
The user plays a game of hog against the computer
'''

#Import statments always go at the top of your code
import random

def roll_dice(num_dice):
    #returns the total number of point earned for rolling that number of dice
    #returns the sum of the Dice. If any ones are rolled, return a score of 1 
    
    #checks to make sure the user entered a legal number of dice
    if (num_dice > 10) or (num_dice < 1):
        print("Warning, incorrect number of dice")
        points = 0
        return points
    points = 0
    
    for i in range(num_dice):
        roll = random.randrange(1,7,1)
        #if a one is rolled, points for that round = 1
        if roll == 1:
            points = 1
            return points
        #somes the number of dice for total points in that round
        points = points + roll
    return points
    

def take_turn(score, opponent_score, num_dice):
    #Calls roll_dice to play one turn of hog, returns the number of points accumulated that round
    
    #checks to see if the sum of the players scores end in 7, if it does only one die is rolled this turn
    if (score + opponent_score) % 10 == 7: #ends in 7:
        points = roll_dice(1)
        return points
    #evaluates the turn
    else:
        points = roll_dice(num_dice)
        return points
    

def roll_3_unless_close_to_end(score, opponent_score, goal_score):
    '''
 describes how the opponent acts, and returns the number
of dice (num_dice) that the player chooses to roll on that turn (between 1 and 10). 
'''
    #if the the human's score is within six of the goal score and computer's score is less than 70% of the goal score, then the roll 7 dice
    if score >= goal_score - 6 and opponent_score < goal_score * 0.7:
        num_dice = 7
        return num_dice
    
   #if the computer's score is greater than 90% of the goal score, then the computer will roll 2 dice
    elif opponent_score > goal_score * .9:
        num_dice = 2
        return num_dice
    
    #otherwise the default is to roll three dice
    else:
        num_dice = 3
        return num_dice
    

def human_player(score, opponent_score, goal_score):
    '''
    strategy function for the human, asks for input of how many dice to roll, returns num_dice
    '''
   
    print("Your score is ",score, " and your opponent's score is ",opponent_score)
    
    numberAsAString = input("Enter in the number of dice to roll (0-10): ")
    num_dice = int(numberAsAString)
    return num_dice


def play_hog(goal_score, max_rounds, strategy1, strategy2):
    '''
 takes goal_score, max_rounds, strategy1, and strategy2 from main function and plays the game of hog until one player wins or the number of rounds expires. Returns 1 if the human player wins, -1 if the computer wins, and 0 if the players tie.
 
 
'''
    score = 0
    opponent_score = 0
    for i in range(max_rounds): 
        num_dice = strategy1(score, opponent_score, goal_score)
        score += take_turn(score, opponent_score, num_dice)
        if score >= goal_score:
            print('Congrats!!! You Win! Your Score = ',score, "Your Opponent's Score = ", opponent_score)
            return 1
        num_dice = strategy2(score, opponent_score, goal_score)
        opponent_score += take_turn(score, opponent_score, num_dice)
        if opponent_score >= goal_score:
            print('You Lost! Better Luck Next Time Your Score = ',score, "Your Opponent's Score = ", opponent_score)
            return 0
    
    #Checks to see if the human player had more points than the computer player if max_rounds expires   
    if score > opponent_score:
        print('Congrats!!! You Win! Your Score = ',score, "Your Opponent's Score = ", opponent_score)
        return 1
    #Checks to see if the computer player had more points than the human player if max_rounds expires   
    if opponent_score > score:
        print('You Lost! Better Luck Next Time Your Score = ',score, "Your Opponent's Score = ", opponent_score)
        return -1
    #Checks to see if the human player and the computer player tied 
    if opponent_score == score:
        print('You Tied! Your Score= ',score, "Your Opponent's Score = ", opponent_score)
        return 0
        
      
        
    
    
def main():
    '''
runs the main function
gets input from user of goal_score and max_rounds, and passes those numbers as integers to play_hog 
will pass human_player strategy and roll_3_unless_close_to_end strategy to play_hog as parameters

'''
    print('Welcome To Hog!')
    goal_score_string = input('What would you like to play to? ')
    goal_score = int(goal_score_string)
    max_rounds_string = input("How many rounds? ")
    max_rounds = int(max_rounds_string)
    play_hog(goal_score, max_rounds, human_player, roll_3_unless_close_to_end)
    
    

# These lines will allow you to run your code from the command line
# But if you just import your code into the python interpreter, 
# it won't run automatically
if __name__ == '__main__':
    main()
            