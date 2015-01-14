import json
address_book = {}
def main():



	# Main is an entry point and defines a function. Multiple functions and be defined within a file.

	while True:

		# While True: Creates a loop. Loop must eventually close. 

		choice = raw_input("What do you want to do? add entry, remove entry, show list, or save and exit? \n  ")               

		# Choice MUST be tabbed - tab after each colon.

		if choice == "add entry":

			fp = open('people.txt', 'r+')

			name = raw_input("What is the name of the person you would like to add? \n")

			number = raw_input( "What is the number of the person you would like to add? \n") 

			address_book[name] = number

			print name + " added to list."

		elif choice == "remove entry":

			removed_entry = raw_input("Which entry would you like to remove? \n")

			del address_book[removed_entry]

			print removed_entry + " Removed from list."

		elif choice == "show list":

			for key in sorted (address_book.keys()):

				print key, address_book[key]

				

		elif choice == "save and exit":


			fp =open('people.txt', "w")
			json.dump(address_book,fp)
			fp.close()
			
			
			

			print "Your file has been updated, thanks for using this program!"

			break

		
			
			

		else: 

			print "I don't understand that command." 

		








main()
 







