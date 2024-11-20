from random import * #   *-ALL FUNC-S,      randit as rd
from math import *

#ülesanne 1
print("bulka")
nimi = input("Tell me your name, and I'll tell what's your name. Don't believe me? Try and press Enter! ")  #lower(), upper(),capitalize()
print("Your name is",nimi+"!")
vanus = int(input("I also can guess your age! so... input your age and press Enter. "))
print("Your age is",vanus,"haha! See, "+nimi+" I know everything about you! (without f, int only with ,,)")
print(f"Your age is {vanus} haha! See, {nimi} I know everything about you! (made with f)")

#Ülesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))

#Ülesanne3
kommid = randint(1,100)
print("There're",kommid,"candies on the table. How much do you want?")
mitu = int(input())
kommid = kommid - mitu
print("Now there're",kommid,"candies left")

#Ül.4
d = float(input("Give me diameter and I'll give you circumference..."))
pi = 3.14
r = (d/2)
c = (2*r*pi)
print(c)

#Ül.5
print("Give me length of the sides of a rectangular plot and I'll give you diagonal")
a = float(input())
b = float(input())
d = ((a**2)+(b**2))**0.5
print(d)

#Ül.6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus

print(f"Sinu kiirus oli {kiirus} km/h")

#Ül.7
print("Give 5 numbers and I'll find the average...")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

av = (a+b+c+d+e)/5
print(av)






