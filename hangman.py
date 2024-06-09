from hangmanUtilities.words import words
from hangmanUtilities.visuals import lives_visual_dict
import random 

def findValidWord():
    word = random.choice(words)
    while " " in word or "-"  in word:
        word = random.choice(words)
    return word

def game():
    word = findValidWord()
    letters_picked=set()
    letters_in_word=set(word)
    lives = 7
    letter_right=set()
    while len(letter_right) != len(letters_in_word) and lives > 0:
        show_word= [letter if letter in letters_picked else '-' for letter in word]
        print('Current word: ', ' '.join(show_word))
        print(lives_visual_dict[lives])
        #print(len(letter_right) == len(letters_in_word), word)
        userInput= input("Please pick  a letter!:  ")
        if len(userInput) == 1 and userInput.isalnum():
            userInputL = userInput.lower()
            if userInputL not in letters_picked:
                letters_picked.add(userInputL)
                if userInputL in word:
                    print(f"Correct! The letter {userInputL} is in the secret word!")
                    letter_right.add(userInputL)
                else:
                    lives = lives-1
                    print(f"Wrong! The letter {userInputL} is not in the secret word!")
            else:
                print("You have already inserted this character")
        else:
            print("This character is not valid, try again!")
    print('Current word: ', word)
game()