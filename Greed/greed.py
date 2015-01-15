import sys
max_players = 10

def clear_screen():
	sys.stdout.write('\033[2J')
	sys.stdout.write('\033[H')
	sys.stdout.flush()

def main():
	clear_screen()

	print "Welcome to Greed!"

	print "How many players are there today?"
	
	num_players = raw_input("Please enter a number between 2-%d! >  " % max_players)
	
	num_players = int(num_players)	

	while num_players not in range(2, (max_players + 1)):
		num_players = raw_input("Please enter a number between 2-%d! >  " % max_players)	
		num_players = int(num_players)	
	


	
	print num_players
	print type(num_players)



	









main()
