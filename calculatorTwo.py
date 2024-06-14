from tkinter import * 
from tkinter.ttk import *

window= Tk()
pad=[
 [{
     "text":"CE",
     "type":"func",
     "width":3,
  },{
     "text":"C",
     "type":"func",
     "width":3,
  },{
     "text":"DEL",
      "type":"func",
     "width":3,
  },{
     "text":"/",
     "type":"func",
     "width":3,
  }] ,
  [{
     "text":"7",
     "width":3,
     "type":"num",
  },{
     "text":"8",
     "width":3,
     "type":"num",
  },{
     "text":"9",
     "width":3,
     "type":"num",
  },{
     "text":"X",
     "width":3,
     "type":"op",
  }],[{
     "text":"4",
     "type":"num",
     "width":3,
  },{
     "text":"5",
     "type":"num",
     "width":3,
  },{
     "text":"6",
     "type":"num",
     "width":3,
  },{
    "text":"-",
    "type":"op",
    "width":3,
  }],[{
     "text":"1",
     "type":"num",
     "width":3,
  },{
     "text":"2",
     "type":"num",
     "width":3,
  },{
     "text":"3",
     "type":"num",
     "width":3,
  },{
    "text":"+",
    "type":"op",
    "width":3,
  }],[{
     "text":",",
     "type":"num",
     "width":3,
  },{
     "text":"0",
     "type":"num",
     "width":3,
  },{
    "text":"=",
    "type":"op",
    "width":6,
  }]
]

def handleOps(row, column, action_kind):
    pass

for row in range(len(pad)):
    for col in range(len(pad[row])):
        btn= Button(text=pad[row][col]['text'], width=pad[row][col]["width"],  command=lambda row=row, column=col, action_kind=pad[row][col]["type"]:handleOps(row, column, action_kind))
        btn.pack()

window.mainloop()