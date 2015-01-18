# Greed
#
# A multi-player Linux terminal implementation of the Greed dice game.
#
# For rules see http://en.wikipedia.org/wiki/Farkle
#
# House rules: 6 dice, 1's are high, no additional points for sets > 3,
# play to 10,000 and max players by default is 10.
# 
# Created by Joshua Ferdaszewski and Katherine Rea
# For the PDX Code Guild Dev Bootcamp
#

import sys
from collections import Counter
from random import randint

max_players = 10
winning_score = 10000
num_dice = 6

# dice ASCII art dict
ascii_dice = {1:"""
 _____
|     |
|  o  |
|     |
 -----""",
2:"""
 _____
|   o |
|     |
| o   |
 -----""",
3:"""
 _____
|   o |
|  o  |
| o   |
 -----""",
4:"""
 _____
|o   o|
|     |
|o   o|
 -----""",
5:"""
 _____
|o   o|
|  o  |
|o   o|
 -----""",
6:"""
 _____
|o   o|
|o   o|
|o   o|
 -----"""}


def clear_screen():
    # ANSI excape sequence to clear screen and reset cursor to top left
    sys.stdout.write('\033[2J')
    sys.stdout.write('\033[H')
    sys.stdout.flush()

    # TODO: print out current score at top of screen with game name


def winner(players):
    # Check each players score and if it is greater than or equal to winning score, return player name
    # Otherwise return None.
    for player in players:
        if player['score'] >= winning_score:
            return player
    return None


def roll(dice):
    # Roll the non held dice
    raw_input("\nPress Enter to roll the dice!")
    for die in dice:
        if die['held'] == False:
            die['value'] = randint(1,6)
    display_dice(dice)
    return


def display_dice(dice):
    # display each die, it's index, and if it is already held
    for i, die in enumerate(dice):
        print ascii_dice[die['value']]
        print "Index: %d Held: %s" % (i, die['held'])
    print "\n"


def check_busted(dice):
    # iterate over the dice, check for scoring patterns. Return True if no dice are pointers; false otherwise.
    pass


def dice_score(dice):
    # Return score of dice, 0 for no score
    # Argv could be a list of values or a list of dice dictionaries
    if isinstance(dice[0], dict):
        # create a list of dice values to score
        dice_to_score = [die['value'] for die in dice if die['held'] == False]
    else:
        dice_to_score = dice

    score = 0
    for num, qty in Counter(dice_to_score).items():    
        # Add score for sets of three (force floor division for >1 sets of 3)
        if qty >= 3:
            if num != 1:
                score += (num * 100) * (qty // 3)
            else:
                score += 1000 * (qty // 3)

        # Add score for 1's and 5's (excluding any scored as a triple set)
        if num == 1:
            score += 100 * (qty % 3)
        elif num == 5:
            score += 10 * (qty % 3)
    return score


def player_turn(players, player_index):
    
    # Initialize dice and turn score at the start of the new turn
    dice = []
    for die in range(num_dice):
        dice.append({'value': 0, 'held': False})
    turn_score = 0
    player_name = players[player_index]['name']
    clear_screen()
    print "%s it is your turn!" % player_name
    
    # Turns can have 1-infinite rounds.
    roll(dice)
    while True:
        # Get current turn score + dice just rolled to display to player
        temp_dice_score = dice_score(dice)
    
        # If busted, user losses all points earned this turn and the turn is over!
        if temp_dice_score == 0:
            print "You have busted! You lost %d potential points because of your GREED!" % turn_score
            raw_input("Press Enter to end your turn. ")
            return

        # There are some points to be had! What does the user want to do?
        decision = raw_input("End turn and score %d points? (end)\n\t\tOR\nSelect dice to hold, and roll again? (roll)\n\n(end/roll) > " % (turn_score + temp_dice_score))
        decision = decision.lower() 

        # End of turn. Take all points earned this turn plus current dice and add to user score
        if decision == "end":
            turn_score += temp_dice_score

            # Add turn score to player score and end this turn!
            players[player_index]['score'] += turn_score
            print "\n%s earned %d points this turn!\nFor a total score of %d!" % (player_name, turn_score, players[player_index]['score'])
            raw_input("\nPress Enter to end your turn. ")
            return

        # User will try their luck and roll again!
        elif decision == "roll":

            # Select dice to hold, and dice to roll again. Check that all held dice are pointer dice.
            while True:
                clear_screen()
                display_dice(dice)
                print "Select die/dice to hold (enter the index of dice to hold, separated by a comma)"
                selection = raw_input("> ")

                # Validate user input - dice_index is a list of ints that are the index of the dice selected by user
                try:
                    dice_index = selection.split(',')
                    dice_index = [int(die_index.strip()) for die_index in dice_index]
                    dice_to_hold = [dice[die_index]['value'] for die_index in dice_index if dice[die_index]['held'] == False]
                    roll_score = dice_score(dice_to_hold)
                except:
                    clear_screen()
                    raw_input("Invalid input. Press Enter and try again. ")
                    continue

                # if selected dice are scoring dice
                clear_screen()
                if roll_score > 0:
                    turn_score += roll_score

                    # Mark scored dice as held
                    for i in dice_index:
                        dice[i]['held'] = True
                    roll(dice)
                    break
                else:
                    raw_input("Non scoring dice selected. Press Enter and try again. ")
                    continue

        # Player typed an invalid selection
        else: 
            print "Invalid selection, try again!"

    # turn is over, print scores and continue to next player
    raw_input("%d, your turn is over. Press enter to continue")
    clear_screen()


def print_scores(players):
    # TODO: print player scores
    pass

def main():
    clear_screen()

    print "\t\tWelcome to Greed!\n"

    print "How many players are there today?"
    
    num_players = raw_input("Please enter a number between 2-%d! >  " % max_players)
    
    num_players = int(num_players)  

    while num_players not in range(2, (max_players + 1)):
        num_players = raw_input("Please enter a number between 2-%d! >  " % max_players)
        num_players = int(num_players)

    players = []
    for player in range(1, num_players + 1):
        player_name = raw_input("Name of player %d > " % player)
        players.append({'name': player_name, 'score': 0})

    # TODO: Randomly select starting player
    current_player = 0

    # Game control loop
    winning_player = None
    while winning_player == None:
        player_turn(players, current_player)
        current_player = (current_player + 1) % num_players
        winning_player = winner(players)

    clear_screen()
    print "Congratulations %s! You are the winner!" % winning_player
    print_scores(players)

    print "Thank you for playing Greed! Goodbye.\n\n"


main()