import string


vokaali=["a","e","u","o","i"]
konsonanti="qwrtpsdfghjklzxcvbnm"

mrkid=string.punctuation


while True:
    v=k=m=t=0
    text=input("sisesta tekst ").lower()
    if text.isdigit():
        break
    else:
        text_list=list(text)
        print(text_list)
        for letter in text_list:
            if letter in vokaali:
                v+=1
            elif letter in konsonanti:
                k+=1
            elif letter in mrkid:
                m+=1
            elif letter == " ":
                t+=1
    print(f"Vokaali {v}")
    print(f"Konsonanti {k}")
    print(f"Markid {m}")
    print(f"Tuhikud {t}")


##############

names=[]

for i in range(5):
    nimi=input(f"{i+1} Nimi: ")
    names.append(nimi)
print(names)
names.sort()
print(names)
print(f"the last added is {nimi}")

v=input("Muudame nimi. Kas nimi vo positsioon? (n/p) ").lower()
if v== "p":
    print(f"sisesta nimi asukoht \n {names}")
    v=int(input())
    print(names[v-1])
    uus=input("uus nimi:")
    names[v-1]=uus
    print(names)


else:
    print(f"sisesta nimi  \n {names}")
    vana_nimi=input("vana nimi ")
    v=names.index(vana_nimi)
    print(names[v])
    uus=input("uus nimi:")
    names[v]=uus
    print(names)

#####################

#dublikatid1
dublta=list(set(names))
print(dublta)

#dublikatid2
dublta=[]
for nimi in names:
    if nimi not in dublta:
        dublta.append(nimi)
print(dublta)

##########
age=[]
print("write ages")
for i in range(7):
    inage=int(input(f"{i+1} age:"))
    age.append(inage)

print(age)
maximum=max(age)
minimum=min(age)
average=sum(age)/len(age)
print(f"max is {maximum}\nmin is {minimum}\naverage is {average}")

################

a=" "
numbers=[11,24,5,23,17]

while a != "end":

    s=input("symbol: ")
    for n in numbers:
        print(n*s)
    a=input("type END to quit or any key to go on    ").lower()

#####################

index=[1,2,3,4,5,6,7,8,9]
maakonnad=["Tallinn","Narva+Narva-Joesuu", "Kohtla-Jarve", "Ida-Virumaa+Laane-Virumaa+Jogevamaa","Tartu linn", "Tartumaa, Polvamaa, Vorumaa, Valgamaa", "Viljandimaa, Jarvamaa, Harjumaa, Raplamaa","Parnumaa","Laanemaa, Hiiumaa, Saaremaa"]
maakonnad_data = dict(zip(index, maakonnad))
print(maakonnad_data)
a=int(input("Testing new function. Give a number  "))
print(maakonnad_data[a])

#############
while 1:
    try:
        ind=int(input("Give an postindex"))
        if len(str(ind))==5:
            break
        else:
            print("!!! 5")
    except ValueError:
        print("!!!")

index_list=list(str(ind))
s1=int(index_list[0])
print(f"Postindex {ind} on {maakonnad[s1-1]}")

