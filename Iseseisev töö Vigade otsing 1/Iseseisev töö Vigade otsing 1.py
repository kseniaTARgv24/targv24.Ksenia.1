from math import *                                     #import * from math

print("Ruudu karakteristikud")
a=input('Sisesta ruudu külje pikkus => ')
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)                            #print("Ruudu ümbermõõt'', P)
di=a*math.sqr(2)
print("Ruudu diagonaal", round(di,2), "\n")            #добавила перенос строки
# print()
print("Ristküliku karakteristikud")                    #print("Ristküliku karakteristikud"))
b=input("Sisesta ristküliku 1. külje pikkus => ")
c=input("Sisesta ristküliku 2. külje pikkus => ")
S=b*c
print("Ristküliku pindala", S)                        #print(Ristküliku pindala', S)
P=2(b+c)
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di), "\n")         #print("Ristküliku diagonaal", round(di)
# print("\n")                                          #эта строчка не нужна

print("Ringi karakteristikud")
r=input("Sisesta ringi raadiusi pikkus => ")           #r=input(''Sisesta ringi raadiusi pikkus => ''))
d=2*r                                                  #d=2r
print("Ringi läbimõõt", d)                             #print("Ringi läbimõõt" d)
S=pi()*r*2
print("Ringi pindala", round(S))
C=2*pi()*r                                             #C=2pi()*r
print("Ringjoone pikkus", round(C)
