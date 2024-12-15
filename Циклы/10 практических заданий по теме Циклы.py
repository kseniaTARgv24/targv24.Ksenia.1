#ul.2

while True:
    try:
        A=int(input("Give A:"))
        break
    except:
        print("natural number please")

summa=0

if A>0:
    for i in range(1,A+1,1):   #including A
        summa +=i
        print(f"{i}.summ {summa}")
    print (f"Answer {summa}")


#ul.3
p=1
for j in range(8):
        while True:
            try:
                number=float(input(f"Give {j+1} number: "))
                break

            except:
                print("give real number")
        if number>0: p*=number
        print(f"{j}.samm {p}")
print(f"Answer {p}")

#ul.4
for i in range (10,20,1):
        print(i**2, end=", ")

#ul.16
for j in range(1, 10):
    for i in range(1,10):
            if i==j:
                print(j, end= " ")         #end- иначе будет сноска строки
            else:
                print("0", end = " ")          
    print()

#ul.15
for j in range(1,11,1):
    for i in range(1,10,1):
        print(i, end=" ")
    print()

#ul.29
for j in range(0,9,1):
    for i in range(0,9,1):
        if i==j or i==0:
            i="x"
            print(i, end = " ")
        else:
            print("0", end=" ")
    print()

#ul.31
k=int(input("vsego kotlet: "))
m=int(input("pomešaetsja na skovorodke: "))
count=0

while(k>=m):
        k-=m
        count+=1

c=m-k
print(f"Polnõe skovorodki: {count}\n I ostanetsja kotlet: {c}")



