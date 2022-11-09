# This is the first hand on practice on the 30DaysOfDataScience
# It aims at exploring some of python data types, data structures and functionality
import random

def rock_paper_scissors():
    '''
        Rock paper scissors is a hand game originating from China, usually played 
        between two people, in which each player simultaneously forms one of three 
        shapes with an outstretched hand.
        The logic of this game is paper beats rock, rock beats scissors but scissors 
        beats paper. The same guess is considered a tie

        arg:
            NaN
        return:
            'Invalid input','A tie','You won' or 'Try again'            
    '''

    items = ['rock','paper','scissors']
    computer_choice = random.choice(items)
    player1_input = input('What\'s your guess? rock, paper or scissors: ').lower()

    # Check for input correctness
    if player1_input not in items:
        return 'Invalid input \'{}\''.format(player1_input)

    print('You choosed {}, and the computer choosed {}'.format(player1_input, computer_choice))
    if player1_input == computer_choice:
        return 'A Tie'
    elif ((player1_input == 'paper' and computer_choice == 'rock') or
            (player1_input == 'rock' and computer_choice =='scissors') or 
            (player1_input=='scissors' and computer_choice=='paper')):
        return '{} beat {}, You Won!!!'.format(player1_input, computer_choice)
    else:
        return '{} beat {}, Try Again'.format(computer_choice, player1_input)
        
       
# Running Session
play_session = True
while play_session ==True:
    print(rock_paper_scissors())
# Determine game termination
    game_contination = input('Are you going for another round:[y/n] ').lower()
    if game_contination == 'n':
        play_session = False
