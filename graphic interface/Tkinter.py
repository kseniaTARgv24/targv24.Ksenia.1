from tkinter import *
from MatplotlibLesson import *

global Color, text, a

def color_choise(a):

    Color = "white"

    if a == 1:
        if text.get() != ' ':
            text.configure(bg="white")
            Color=text.get()
        
        else:
            text.configure(bg="red")
        
    return Color
        


def figure(Color: str):
    # global color
    color_choise()
    choise=var.get()
    if choise==1:
        Vaal(Color)
    elif choise ==2:
        Vihmavari(Color)
    else:
        print("Nothing yet")
    a = 0



root = Tk()
root.geometry("400x400")
root.title("Graphs")

name=Label(root, text="Graphs!", font="beer_money 15",fg="deep pink").pack(pady = 20)

# name.pack(...)

var=IntVar()
r1=Radiobutton(root, text="Vaal", font="beer_money 15", variable=var, value=1, command=figure)
r2=Radiobutton(root, text="Vihmavary", font="beer_money 15", variable=var, value=2, command=figure)

text=Entry(root, font="beer_money 15", fg = "deep pink", bg="white", width=100)
b=Button(root,text = "Color choise", font="beer_money 15", command=color_choise(1))

# name.pack()
r1.pack()
text.pack()
r2.pack()
b.pack()





root.mainloop()