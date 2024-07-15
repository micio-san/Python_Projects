#User inputs the lower bound and upper bound of the range.
#The compiler generates a random integer between the range and store it in a variable for future references.
#For repetitive guessing, a while loop will be initialized.
#If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
#Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
#And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
#Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.

import random
import math

def get_lower_and_upper(lower):
    while True:
     bound = input(f"Gimme {"lower" if lower else "upper"} bound: ")
     if bound.isdigit():
         if int(bound)>=0:
             return int(bound)
         else:
             print("The bound must be bigger than 0")
     else :
        print("The bound must be a number")

def main():
    lower = get_lower_and_upper(True)
    upper = get_lower_and_upper(False)
    if lower > upper:
        print("The lower bound must be smaller than the bigger bound!")
        lower = get_lower_and_upper(True)
        upper = get_lower_and_upper(False)
    randomInt = random.randint(lower, upper)
    chances = math.ceil(math.log(upper - lower + 1, 2))
    print(f"You have a total of: {chances} chances!")
    tries=0;
    win=False
    while  chances >= tries or win==True:
        print(tries, randomInt)
        guess= input(f"Guess a number between {lower} and {upper}")
        if guess.isdigit():
            guess = int(guess)
            if lower < guess < upper:
                if guess == randomInt:
                  win=True
                elif guess > randomInt :                    
                    tries=tries+1;
                    print(f"Try Again! You guessed too high, but  you still have {chances -tries} tries")  if tries != chances else print("")
                else:
                    tries=tries+1;
                    print(f"Try Again! You guessed too small but you still have {chances -tries} tries") if tries != chances else print("")
            else:
               input(f"Guess a number between {lower} and {upper}!")
        else:
            print(f"The solution is a number!")
    else: 
        print("You do not have any more chances! D:") if tries > chances else  print("You win!")


if __name__== "__main__":
    main()

