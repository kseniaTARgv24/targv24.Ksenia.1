
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
print(f"{vastus} 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. {vastus*2} eur")

print("\nUl.5\n")
word1 = "Kill"
word2 = "Koll"
word3 = "Killadi"
try:
    result = f"{word1}-{word2} {word1}-{word2} {word3}-{word2} {word1}-{word2} {word1}-{word2} {word3}-{word2} {word1}-{word2} {word1}-{word2} {word1}-{word2}\n{word1}-{word2}"
    print(result.upper())
except Exception as e:
    print(f"Viga: {e}")


print("\nUl.6\n")
song = """
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""
try:
    print(song.upper())
except Exception as e:
    print(f"Viga: {e}")


print("\nUl.7\n")
try:
    pikkus = float(input("Sisesta ristküliku pikkus: "))
    laius = float(input("Sisesta ristküliku laius: "))
    ümbermõõt = 2 * (pikkus + laius)
    pindala = pikkus * laius
    print(f"Ristküliku ümbermõõt on {ümbermõõt} ja pindala on {pindala}.")
except Exception as e:
    print(f"Viga: {e}")


print("\nUl.8\n")
try:
    kütus = float(input("Sisesta tangitud kütuse hulk liitrites: "))
    kilomeetrid = float(input("Sisesta läbitud kilomeetrite arv: "))
    kulu_100km = (kütus / kilomeetrid) * 100
    print(f"Kütusekulu 100 km kohta on {kulu_100km:.2f} liitrit.")
except Exception as e:
    print(f"Viga: {e}")


print("\nUl.9\n")
try:
    kiirus = 29.9
    minutid = float(input("Sisesta rulluisutamise aeg minutites: "))
    kaugus = kiirus * (minutid / 60)
    print(f"Rulluisutaja jõuab {minutid} minutiga {kaugus:.2f} km kaugusele.")
except Exception as e:
    print(f"Viga: {e}")


print("\nUl.10\n")
try:
    minutid = int(input("Sisesta aeg minutites: "))
    tunnid = minutid // 60
    ülejäänud_minutid = minutid % 60
    print(f"{minutid} minutit on {tunnid}:{ülejäänud_minutid}.")
except Exception as e:
    print(f"Viga: {e}")


