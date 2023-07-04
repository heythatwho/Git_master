#slot machine testing
import random

MAX_LINES =3 #assign a constant value,not gonna change
MAX_BET=100
MIN_BET=1

ROWS =3
COLS=3

symbol_count = {
	"A": 2,
	"B": 4,
	"C": 6,
	"D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
	#randomly select values here
	all_symbols =[]
	for symbol, symbol_count in symbols.items():
		for _ in range(symbol_count):
			all_symbols.append(symbol)

	#columns = [[],[],[]]
	columns = []
	for col in range(cols):
		column=[]
		current_symbols =all_symbols[:] #copy a list, dont want to impact the variable
		for _ in range(rows):
			value = random.choice(all_symbols)
			current_symbols.remove(value)

		columns.append(column) 
	return columns
	
def print_slot_machine(columns):#need to rotate to vertical
	for row in range(len(columns[0])): #loop through every singele row we have
		for i, column in enumerate(columns): #for every single row, we loop to every column
			if i != len(columns) -1 : #for every column we only print the current row we are on
				print(column[row], end=" | ")
			else:
				print(column[row], end ="")
		print()


#create deposit function
def deposit():
	while True:
		amount=input("what would you like to deposit? $")
		if amount.isdigit(): #ensure valid whole number, or else next step fails
			amount= int(amount)
			if amount >0:
				break
			else:
				print("Amount must be greater than 0")

		else:
			print("please enter a number.")
	return amount


#collect the bet
def get_number_of_lines():
	while True:
		lines=input("enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
		if lines.isdigit():
			lines=int(lines)
			if 1 <= lines <= MAX_LINES:
				break
			else:
				print("enter a valid number of lines")
		else:
			print("please enter a number.")
	return lines

#get amount of each bet
def get_bet():
	while True:
		amount=input("what would you like to bet on each lines? $")
		if amount.isdigit(): #ensure valid whole number, or else next step fails
			amount= int(amount)
			if MIN_BET<= amount <= MAX_BET:
				break
			else:
				print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")

		else:
			print("please enter a number.")
	return amount

#Call the function again once it is done, we can ask for input again see if they want to play again
def main():
	balance = deposit()
	lines =get_number_of_lines()
	while True:#check the bet amount within their total balance
		bet =get_bet()
		total_bet =bet * lines

		if total_bet> balance:
			print(f"you dont have enough to bet that amount, your current balance is ${balance}")
		else:
			break
	print(f"you are betting  ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

	#print(balance, lines, bet)
	slots = get_slot_machine_spin(ROWS,COLS, symbol_count)
	print_slot_machine(slots)

main()
