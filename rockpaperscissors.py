import random

playerScore=0
computerScore=0
MAX=3
CHOICES=['r','p','s']

def confront(player,pc):
        global playerScore 
        global computerScore
        if player == pc:
              playerScore= playerScore
              computerScore=computerScore
        elif (player == 'r' and pc == 's') or (player == 's' and pc == 'p') or (player == 'p' and pc == 'r'):
              playerScore += 1
        else: 
              computerScore += 1
              

            

def checkValue():
        value = input("Insert r for rock, p for paper and s for scissors")
        computer = random.choice(CHOICES)
        print("mi/pc", value, computer)
        if(value.lower() in CHOICES):
           confront(value, computer)
        else:
           print("The value inserted is not correct!")
                
                

def game():
        cow = 0
        global playerScore 
        global computerScore
        global MAX
        while (playerScore + computerScore)<MAX:
          checkValue()
          cow+=1
       
        finalRes = f"Player wins with: {playerScore}" if playerScore> computerScore else f"Computer wins with: {computerScore}"
        print(finalRes)

game()
