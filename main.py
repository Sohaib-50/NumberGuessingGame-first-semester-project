FE Batch 2019
A, B, C, D
Due Jan 2, 11:59 PM
Assignment 01
20 points

Dr. Maria Waqas
Dec 13, 2019 (Edited Jan 2)
This assignment is a marked work. It carries 20 marks which will be scaled down to 7 marks in sessional score.
You are not supposed to upload anything here. This is just a reminder for submission deadline. 
Class comments

Your work
Turned in

CS19096.py
Text
Private comments


from time import sleep

#Main function:

def main():
	OPTIONS = list(range(-122, 166, 3)) #initialize the list of numbers we'll be working on.
	print(f"{'~WELCOME TO THE GUESSING GAME~' : ^75}\n")
	while True:
		mn, mx = 0, len(OPTIONS) - 1
		guesses = 1
		print("Chose a number from the list of numbers given below, and I’ll guess it in\nno more than 7 tries.\n")
		print("Please answer any question asked in terms of y/Y or n/N ONLY depending on\nwhether the question asked is correct or wrong respectively.")
		display_list(OPTIONS, 4) #displays OPTIONS in a pretty format
		print()
		input("Choose a number from the list above and then press ENTER whenever you are ready.... ")
		print("OK let's begin, in:")
		display_countdown(3) #displays count down from 3 to 1
		print("." + "\n" * 2)

		while mx >= mn: 
			print()
			mid_index = (mx + mn) // 2
			try_guess = OPTIONS[mid_index]
			user_response = input_yesno(f"//Did you choose  the number {try_guess}?  ")
			print()
			if user_response == "y": #guess was correct
				print("\n" * 2)
				print(f"!!!YOUR NUMBER WAS {try_guess}!!!")
				print(f"It took me {guesses} guess(es) to guess your number.")
				break
			else: #guess was wrong
				guesses += 1 #increment number of guesses
				user_response = input_yesno(f"//Is your chosen number greater than {try_guess}?  ")
				if user_response == "y": #answer lies in right half of current list being considered
					mn = mid_index + 1 #disregard bottom half of list by moving bottom-of-list pointer to one position ahead of the middle index
				else: #answer lies in right half of current list being considered
					mx = mid_index - 1  #disregard bottom half of list by moving top-of-list pointer to one position behind the middle index.
		else: #this else will be executed when mx becomes larger than mn or vice versa (when while loop exits without break statement)
			print()
			print("Stopping.")
			print("You are either cheating, or making a mistake.")
			
		print(".\n" * 5)
		if input("Press y/Y if you want to play again: ") not in ['y',  'Y']: #if anything other than y/Y, exit program
			print("\n" * 3)
			print("Exit-ing. Have a good day. Bye!")
			input() #to prevent window from closing immedietly after end of program.
			break
		else: #restart the game (will go to start of first while loop after execution of the following block)
			print()
			print("OK, restarting in")
			display_countdown(5)



#User-defined functions:

def display_list(lst, n):
	'''
	Function to output a list in a pretty format. 
	Parameters:
		>lst - the list you want to display
		>n - number of items you want to be displayed per row.
	Return values:
		>None
	'''
	print(" " * 20 + "_" * (n * 8))#leading spaces
	for i in range(len(lst)):
		if i%n == 0:
			if i != 0:
				print("|", end = "")
			print()
			print(" " * 20, end = "")#leading spaces
		print(f"|{str(lst[i]):^7}", end = "")
	print()
	print(" " * 20 + "_" * (n * 8))


def display_countdown(m):
	'''
	Function to display a countdown from m to zero with each number 
	on a new line with a gap of 0.6 seconds between each number.
	Parameters:
		>m - value to be counted down from.
	Return  values:
		>None
	'''
	for i in range(m, 0, -1):
			print(i)
			sleep(0.6)


def input_yesno(prompt):
	'''
	Function to get input from user either y/Y or n/N.
	The parameter prompt will be displayed on screen, and then
	user input will be taken. User will be reprompted till they enter
	either y/Y or n/N, and an error message will be displayed after
	each undesired input.
	Parameters:
		>prompt - the prompt that you want to be displayed just like
		the prompt you give as parameter to the function input().

	Return values:
		>user's answer in lower case.
	'''
	y_n =  input(prompt)
	while y_n.lower() not in ("y", "n"):
		y_n = input(f"Invalid input! Please enter either y/Y or n/N.\n\n{prompt}")
	return y_n.lower()
	

main()
CS19096.py
Displaying CS19096.py.
