from tkinter import * 
from tkinter.ttk import *

window= Tk()
frame = Frame(window)
first_str=StringVar()

pad=[
 [{
     "text":"CE",
     "type":"func",
     "width":4,
  },{
     "text":"C",
     "type":"func",
     "width":4,
  },{
     "text":"DEL",
      "type":"func",
     "width":4,
  },{
     "text":"/",
     "type":"func",
     "width":4,
  }] ,
  [{
     "text":"7",
     "width":4,
     "type":"num",
  },{
     "text":"8",
     "width":4,
     "type":"num",
  },{
     "text":"9",
     "width":4,
     "type":"num",
  },{
     "text":"X",
     "width":4,
     "type":"op",
  }],[{
     "text":"4",
     "type":"num",
     "width":4,
  },{
     "text":"5",
     "type":"num",
     "width":4,
  },{
     "text":"6",
     "type":"num",
     "width":4,
  },{
    "text":"-",
    "type":"op",
    "width":4,
  }],[{
     "text":"1",
     "type":"num",
     "width":4,
  },{
     "text":"2",
     "type":"num",
     "width":4,
  },{
     "text":"3",
     "type":"num",
     "width":4,
  },{
    "text":"+",
    "type":"op",
    "width":4,
  }],[{
     "text":",",
     "type":"num",
     "width":4,
  },{
     "text":"0",
     "type":"num",
     "width":4,
  },{
    "text":"=",
    "type":"op",
    "width":4,
  }]
]

def handleOps(row, column, action_kind):
    pass

for row in range(len(pad)):
    for col in range(len(pad[row])):
        pad[row][col] = Button(text=pad[row][col]['text'], width=pad[row][col]["width"],  command=lambda row=row, column=col, action_kind=pad[row][col]["type"]:handleOps(row, column, action_kind))
        pad[row][col].grid(row=row, column=col)

window.mainloop()