from random import * #   *-ALL FUNC-S,      randit as rd
from math import *

#ülesanne 1
print("bulka")
nimi = input("Tell me your name, and I'll tell what's your name. Don't believe me? Try and press Enter! ")  #lower(), upper(),capitalize()
print("Your name is",nimi+"!")
vanus = int(input("I also can guess your age! so... input your age and press Enter. "))
print("Your age is",vanus,"haha! See, "+nimi+", I know everything about you! (without f, int only with ,,)")
print(f"Your age is {vanus} haha! See, {nimi}, I know everything about you! (made with f)\n\n ")

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
print("\n\nThere're",kommid,"candies on the table. How much do you want?")
mitu = int(input())
kommid = kommid - mitu
print("Now there're",kommid,"candies left")

#Ül.4
d = float(input("\n\nGive me diameter and I'll give you circumference..."))
pi = 3.14
r = (d/2)
c = (2*r*pi)
print(c)

#Ül.5
print("\n\nGive me length of the sides of a rectangular plot and I'll give you diagonal")
a = float(input())
b = float(input())
d = ((a**2)+(b**2))**0.5
print(d)

#Ül.6
aeg = float(input("\n\nMitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus

print(f"Sinu kiirus oli {kiirus} km/h")

#Ül.7
print("\n\nGive 5 numbers and I'll find the average...")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

av = (a+b+c+d+e)/5
print(av) 

#Ül.8
print("\n\n   @..@ \n  (----)\n ( \__/ )\n  ^^ "" ^^  ")  

#Ul.9
print("\n\ngive me 3 sides of a triangle, and I'll calculate its perimeter")
a = float(input())
b = float(input())
c = float(input())
P = (a*b*c)
print("the perimeter is",P)

#Ul. 10
print("\n\nVõtsite P sõbraga suure pitsa hinnaga 12,90€ \nJätate teenindajale 10% jootraha.")
hind = 12.9
joot = hind*0.1
kokku = hind + joot
print("Kokku te leate maksma",kokku,"Utle mulle, kui palju sopru on, ja ma utlen kui palju iga uks peab maksma.")
P = int(input()) # Ставлю здесь инт, чтобы не дать пользователю ввести дробное число людей
P = float(P) #Привожу число людей к тому же типу данных, что и сумму денег
vastus = kokku/P
print("Iga uks peab maksma",vastus,"eur")









