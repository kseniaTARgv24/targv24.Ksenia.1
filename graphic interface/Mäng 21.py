from tkinter import *
from tkinter import messagebox
from turtle import color
from PIL import Image, ImageTk
from numpy import size
import random


root=Tk()
root.geometry("800x500")
root.resizable(False,False)
root.title("21")



def game():
    button1.place_forget()

    a = random.randint(2, 11)
    b = random.randint(2, 11)

    card1.configure(text= str(a))
    card1.place(x=100, y=100)
    card2.configure(text= str(b))
    card2.place(x=500, y=100)
    summa.configure(text=(f"{a+b}"))
    summa.place(x=370, y=30)
    pause.place(x=200, y=400)
    TakeCard.place(x=500, y=400)



def pauseChoisedef():
    card1.place_forget()
    card2.place_forget()
    card3.place_forget()
    ph_label.place(x=0, y=0)
    Continue.place(x=340, y = 360)
    showStartMenu()


def TakeCardChoisedef():
    print("di nahui")
   
def showStartMenu():
    Continue.place_forget()
    ph_label.place_forget()
    pause.place_forget()
    TakeCard.place_forget()
    summa.place_forget()


    button1.place(x=340, y = 360)



original_image = Image.open(r"graphic interface\ttt.png")
resized_image = original_image.resize((800, 500))  # Resize to window size
bgimage = ImageTk.PhotoImage(resized_image)

labelBG=Label(root,image=bgimage)
labelBG.place(x=0,y=0)

button1=Button(root,text="Start",font=("beer money", 45), bg="#36051c", command=game) #command = Start
button1.place(x=340, y = 360)

cardImage=Image.open(r"graphic interface\images.png")
bgCardImage=ImageTk.PhotoImage(cardImage)


card1=Label(root, image=bgCardImage, text="nr",font=("beer money", 45), compound='center')
card2=Label(root, image=bgCardImage, text="nr",font=("beer money", 45), compound='center')
card3=Label(root, image=bgCardImage, text="nr",font=("beer money", 45), compound='center')

ph_label=Label(root, text = "aaaaaaa")

summa=Label(root, bg='pink', text="nr", font=("beer money", 45))

pause=Button(root,text="Pause",font=("beer money", 30), bg="#36051c", command=pauseChoisedef)
TakeCard=Button(root,text="Take card",font=("beer money", 30), bg="#36051c", command = TakeCardChoisedef)
Continue=Button(root,text="Continue",font=("beer money", 30), bg="#36051c", command = showStartMenu)







root.mainloop()

