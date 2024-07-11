MAX_LINES=3
MAX_BET=100
MIN_BET=0

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


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = amount_to_bet()
    print(f"You are betting {str(bet)}$ on {str(lines)} lines for a total amount of {int(bet) * int(lines)}$ and you deposited {str(balance)}$")

if __name__ == "__main__":
    main()