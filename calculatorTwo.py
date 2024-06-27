from calculatorTwoUtilities.pad import pad
from tkinter import * 
from tkinter.ttk import *

window= Tk()
frame = Frame(window)
window.geometry("300x300")
#write first in sec val and when op is called move to second

calculator_screen= StringVar(window)

valueOne=""
labelOne= Label(textvariable=calculator_screen,  font=('consolas',20))
labelOne.grid(row=1, column=3)

valueTwo=""
calculator_screen_sm= StringVar(window)
labelTwo= Label(textvariable=calculator_screen_sm)
showLabelTwo = 0 if len(valueTwo)==0 else 3
labelTwo.grid(row=0, column=showLabelTwo)
evaluated=FALSE

def showValues(value, displayer): {
  displayer.set(value)
}

def handleFunc(row, column):
   global valueOne
   global valueTwo
   global calculator_screen
   global calculator_screen_sm
   global evaluated
   match pad[row][column]["text"]:
       case "=":
        if not evaluated:
         valueTwo += valueOne
         valueOne=eval(valueTwo)
         showValues(valueOne, calculator_screen)
         showValues(valueTwo, calculator_screen_sm)
         evaluated=TRUE
        else:
         return
       case "CE":
         valueOne=""
         valueTwo=""
         evaluated=FALSE
         showValues(valueOne, calculator_screen)
         showValues(valueTwo, calculator_screen_sm)
       case "C":
         valueOne=""
         showValues(valueOne, calculator_screen)
       case "DEL":
         showValues(valueOne, calculator_screen)
         
        
def handleOps(row, column, action_kind):
    global valueOne
    global valueTwo
    global calculator_screen
    global calculator_screen_sm
    match action_kind:
        case "num":
            if not evaluated:
             valueOne += pad[row][column]["text"]
             calculator_screen.set(valueOne)
            else:
               return
        case "op":
            if len(valueTwo) == 0 and not evaluated:
             valueOne+=pad[row][column]["text"]
             valueTwo=valueOne
             calculator_screen_sm.set(valueTwo)
             valueOne=""
             calculator_screen.set(valueOne)
            else:
              return
        case "func":
            handleFunc(row, column)
        
        

for row in range(len(pad)):
    for col in range(len(pad[row])):
        pad[row][col] = Button(text=pad[row][col]['text'], width=pad[row][col]["width"], command=lambda row=row, column=col, action_kind=pad[row][col]["type"]:handleOps(row, column, action_kind))
        pad[row][col].grid(row=row+2, column=col)

window.mainloop()