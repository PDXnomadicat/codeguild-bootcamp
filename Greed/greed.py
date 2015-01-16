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
	# Otherwise return 0. pass in players list of dicts
	for player in players:
		if player[Score] >= winning_score:
			return player

	return 0


def roll(dice):
	# Roll the non held die and return the dice list
	pass

def player_turn(player):
	dice = []
	for die in range(num_dice):
		dice.append({'value': None, 'held': False})

	roll(dice)
	# Score and 



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

	winning_player = 0
	while winning_player == 0:
		player_turn(current_player)
		current_player = (current_player + 1) % num_players
		winning_player = winner(players)

	clear_screen()
	print "Congratulations %s! You are the winner!" % winning_player
	print_scores(players)

	print "Thank you for playing Greed! Goodbye."


main()
