from tkinter import *

def change():
    if var.get() == 0:
        lb['text'] = '+88005553535'
    elif var.get() == 1:
        lb['text'] = '+79358732323'
    elif var.get() == 2:
        lb['text'] = '+89001312323'


root = Tk()

var = IntVar()
var.set(0)
fr1 = Frame()
fr2 = Frame()
rb1 = Radiobutton(fr1, indicatoron=0 , width=10,height=2,text="Вася",
                  variable=var, value=0 ,command=change)
rb1.pack()
rb2 = Radiobutton(fr1, indicatoron=0 ,width=10,height=2, text="Петя",
                  variable=var, value=1,command= change )
rb2.pack()
rb3 = Radiobutton(fr1, indicatoron=0 , width=10,height=2,text="Гриша"
                  ,variable=var, value=2,command= change )
rb3.pack()
lb = Label(fr2,width=30, height=7)
lb.pack()
fr1.pack(side = LEFT)
fr2.pack(side = LEFT)
root.mainloop()