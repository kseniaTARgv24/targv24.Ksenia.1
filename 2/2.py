
from datetime import *
from calendar import *

print("Ul.1\n")
tana = date.today().strftime("%B %d, %Y") #фун-я
print(f"Tere!, Tana on {tana}")
d=date.today().day  #свойство
print(d)
novP=monthrange(2024,11)[1]
detsP=monthrange(2024,12)[1]
jaak=detsP+novP-d
jaak2=novP-d
print(f"Aasta loppuni on {jaak}")
print(f"kuu loppuni on {jaak2}")


print("\nUl.2\n")
a= int( 3 + 8 / (4 - 2) * 4)
b= int( (3 + 8) / (4 - 2) * 4)
c= int( (3 + 8) / 4 - 2 * 4)
d= int( 3 + 8 / 4 - 2 * 4)
print(a)
print(b)
print(c)
print(d)

print("\nUl.3\n")
print("Ruudu sees asub ring. Sisesta raadius")
try:
 R = float(input())
 pi = 3.14
 RuuduS = (R*2)**2
 RuuduÜ = (R*2)*4
 RingiP = pi * (R**2)
 RingiÜ = 2 * pi * R
 print(f"ruudu pindala = {RuuduS}, ruudu ümbermõõt = {RuuduÜ}, ringi pindala = {RingiP}, ringi ümbermõõt = {RingiÜ}")
except:
    print("number!!!")
    

print("\nUl.4\n")
Ümber= 2 * pi * 6378000000 #mm
münt= 25.75
vastus = int(Ümber/münt)
print(f"{vastus} 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa")

print("\nUl.5\n")

