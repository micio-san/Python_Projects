from tkinter import *

operation=""
result=0


def calc_operation(value):
    operation

def delete():
    pass

def reset():
    pass

def calc_action(row, column):
    value=pad[row][column]['text']
    if(value.isnumeric()):
       calc_operation(value)
    elif(value == "CE"):
      pass
    else:
      pass



pad=[
      ["CE", "C", "DEL","÷",],
      ["7","8","9","x"],
      ["4","5","6","-"],
      ["1","2","3","+"],
      ["","0",",","="]
     ]

window= Tk()
window.title("My Calculator")

frame= Frame(window)

for row in range(5):
    for column in range(4):
        pad[row][column]=Button(text=pad[row][column], font=('consolas', 20), command=lambda row=row, column=column: calc_action(row, column), width=3, height=1)
        pad[row][column].grid(row= row, column=column)

window.mainloop()