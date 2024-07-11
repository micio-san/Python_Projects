import random

MAX_LINES=3
MAX_BET=100
MIN_BET=0
ROWS=3
COLS=3

symbols_count={
    "<3":2,
    ":D":4,
    ":)":6,
    ":/":8
}

symbols_values={
    "<3":5,
    ":D":4,
    ":)":3,
    ":/":1
}


def check_winner(cols, lines, bet, values): 
    winnings=0
    winnin_lines=[]
    for line in range(lines):
        symbol = cols[0][line]
        for col in cols:
            symbols_to_check= col[line]
            if symbol != symbols_to_check:
                break
        else:
            #if no break occurs in for loop the this executes
            winnings += values[symbol] * bet
            winnin_lines.append(line + 1)
    return winnings, winnin_lines






def deposit():
    while True:
        amount= input("What would you like to deposit? $")
        if amount.isdigit():
            if int(amount) > 0:
               int(amount)
            else:
                print(f"You cannot deposit less than 1$!")
        else:
            print("Enter a valid value!")
        return amount

def get_number_of_lines():
     while True:
        lines= input(f"Entrer the number of lines to bet on (1-{str(MAX_LINES)})")
        if lines.isdigit():
            if  0 < int(lines) <= MAX_LINES:
                int(lines)
            else:
                print(f"Please enter a number between 1 to {str(MAX_LINES)}!")
        else:
            print("Enter a valid value!")
        return lines

def amount_to_bet():
    while True:
        bet= input(f"Entrer the amount you want to bet between ({str(MIN_BET)}-{str(MAX_BET)})")
        if bet.isdigit():
            if  MIN_BET < int(bet) <= MAX_BET:
                int(bet)
            else:
                print(f"Please enter a number between {str(MIN_BET)} to {str(MAX_BET)}!")
        else:
            print("Enter a valid value!")
        return bet      

def get_slot_machine_spin(row, col, symbols):
    #based on the frequency of symbols in symbols, generate which symbls will be in which column
    all_symbols = [];
    for symbols_values, symbols_keys in symbols.items():
        for _ in range(symbols_keys) :
            all_symbols.append(symbols_values)
    columns=[]
    for _ in range(col):
        column=[]
        current_symbols = all_symbols[:]
        for _ in range(row):
            #copia una lista, seleziona e poi la rimuove e reitera nuovamente
            which= random.choice(current_symbols)
            current_symbols.remove(which)
            column.append(which)
        columns.append(column)
    return columns
  
def print_slot(columns):
    for row in range(len(columns[0])):
        for  i, col in enumerate(columns):
            if i != len(columns) -1:
             #end line when column ended, it's default to \n
             print(col[row], end="|")
            else:
             print(col[row], end="")
        print()

        
def game():
    lines = get_number_of_lines()
    bet = amount_to_bet()
    print(f"You are betting {str(bet)}$ on {str(lines)} lines for a total amount of {int(bet) * int(lines)}$ and you deposited {str(balance)}$")
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot(slots)
    winning, winning_lines = check_winner(slots,int(lines), int(bet), symbols_values)
    #asterisk prints all the values of array without [] and commas
    print(f"You won {winning}, on lines:", *winning_lines)   
    return int(winning) -int(bet) 
#3 in a row

def main():
    balance = deposit()
    while 
 
   

if __name__ == "__main__":
    main()