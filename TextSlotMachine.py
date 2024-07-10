import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def deposit():
    while True:
        amount= input("What would u like to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Invalid amount")
        else:
            print("Invalid value")
    return amount

def get_number_of_lines():
    while True:
        lines= input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines < MAX_LINES:
                break
            else:
                print("Enter a vald line")
        else:
            print("Invalid value")
    return lines

def get_bet():
    while True:
        amount= input("What would u like to bet? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Invalid value")
    return amount

def main(): 
    balance=deposit();
    lines=get_number_of_lines()
    while True:
          bet=get_bet()
          total_bet = bet * lines
          if total_bet > balance:
              print(f"You do not have enough to bet that amount, your current balance is {balance}")
          else:
              break
    print(f"you are betting {bet}$ on {lines} lines, with a total bet of {total_bet}$")

main()