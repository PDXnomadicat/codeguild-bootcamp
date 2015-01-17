import sys
max_players = 10
winning_score = 10000
num_dice = 6

def clear_screen():
    sys.stdout.write('\033[2J')
    sys.stdout.write('\033[H')
    sys.stdout.flush()

def winner(players):
    # Check each players score and if it is greater than or equal to winning score, return player name
    # Otherwise return None.
    for player in players:
        if player['score'] >= winning_score:
            return player
    return None


def roll(dice):
    # Roll the non held die and display results flagging held and displayed
    # in index order with index printed underneath the die
    display_dice(dice)
    pass

def display_dice(dice):
    # Display each die
    pass

def check_busted(dice):
    # iterate over the dice, check for scoring patterns. Return True if no dice are pointers; false otherwise.
    pass

def dice_score(dice_values):
    # Return score with the dice values passed in as a list (return 0 for no score)
    return 1


def player_turn(players, player_index):
    
    # Initialize dice and turn score at the start of the new player's turn
    dice = []
    for die in range(num_dice):
        dice.append({'value': None, 'held': False})
    turn_score = 0
    player_name = players[player_index]['name']

    # User selects whether to end turn or roll again
    while True:
        print "%s it is your turn! Roll your dice!" % player_name
        rolled_dice = roll(dice)
    
        # If busted, user losses all points earned this turn and the turn is over!
        if check_busted(dice) == True:
            print "You have busted! You lost %d potential points because of your GREED!" % turn_score
            return

        # Get current turn score + dice just rolled to display to player
        dice_to_score = []
        for die in dice:
            if die['held'] == False:
                dice_to_score.append(die['value'])
        temp_dice_score = dice_score(dice_to_score)

        # There are some points to be had! What does the user want to do?
        decision = raw_input("End turn and score %d points + current dice roll? (end).\nOR\nSelect dice to hold, and dice to roll again? (roll)\n(end/roll) > " % (turn_score + temp_dice_score))
        decision = decision.lower() 

        # End of turn. Take all points earned this turn plus current dice and add to user score
        if decision == "end":
            turn_score += temp_dice_score

            # Add turn score to player score and end this turn!
            players[player_index]['score'] += turn_score
            print "%s earned %d points this turn!\nFor a total score of %d!" % (player_name, turn_score, players[player_index]['score'])
            return

        # User will try their luck and roll again!
        elif decision == "roll":

            # Select dice to hold, and dice to roll again. Check that all held dice are pointer dice.
            while True:
                print "Select die/dice to hold (enter the index of dice to hold, separated by a comma)"
                display_dice(dice)
                selection = raw_input("> ")

                # Validate user input - dice_index is a list of ints that are the index of the dice selected by user
                try:
                    dice_index = selection.split(',')
                    for i, die_index in enumerate(dice_index):
                        dice_index[i] = int(die_index.strip())
                        if die_index not in range(1, num_dice + 1):
                            raise ValueError
                except:
                    print "Invalid input. Try again."
                    continue

                # Get score of selected dice (if any) and add to turn_score
                roll_score = dice_score(dice_index)
                if roll_score > 0:
                    turn_score += roll_score

                    # Mark scored dice as held
                    for i in dice_index:
                        dice[i]['held'] = True
                    break
                else:
                    print "Non scoring dice selected. Try again."
                    continue

        # Player typed an invalid selection
        else: 
            print "Invalid selection, try again!"




def print_scores(players):
    # TODO: print player scores
    pass

def main():
    clear_screen()

    print "Welcome to Greed!"

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

    print "Thank you for playing Greed! Goodbye."


main()
