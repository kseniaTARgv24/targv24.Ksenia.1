#~_~
from module1 import *
x=" "

a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
S=summa3(a,b,c)
print(S)

print("\n\n7\n")
while x!="STOP":
    while True:
        try:
            a=float(input("a = "))
            b=float(input("b = "))
            c=input("operation = ")
            S=arithmetic(a,b,c)
            print(S)
            break
        except:
            print("error")
    S=is_year_leap(year)
    print(S)
    x=input("type 'stop' to exit or enter to continue  ").upper()


print("\n\n2\n")
while x!="STOP":
    while True:
        try:
            year = int(input("year: "))
            break
        except:
            print("error")
    S=is_year_leap(year)
    print(S)
    x=input("type 'stop' to exit or enter to continue  ").upper()

print("\n\n3\n")
while x!="STOP":
    while True:
        try:
            a=float(input("a = "))
            V=square(a)
            print(V)
            break
        except:
            print("error")
    x=input("type 'stop' to exit or enter to continue  ").upper()

print("\n\n4\n")
while x!="STOP":
    while True:
        try:
            a=int(input("month = "))
            s=season(a)
            print(s)
            break
        except:
            print("error")
    x=input("type 'stop' to exit or enter to continue  ").upper()

print("\n\n5\n")
while x!="STOP":
    while True:
        try:
            a=float(input("вклад = "))
            years=int(input("период (года) = "))
            s=bank(a,years)
            print(s)
            break
        except:
            print("error")
    x=input("type 'stop' to exit or enter to continue  ").upper()


print("\n\n6\n")

while x!="STOP":
    while True:
        try:
            a=float(input("простое ли число? --> "))
            v=is_prime(a)
            print(v)
            break
        except:
            print("error")
    x=input("type 'stop' to exit or enter to continue  ").upper()




print("\n\n7\n")

while x!="STOP":
    while True:
        try:
            print("Insert date in numbers:")
            a=int(input("day  "))
            b=int(input("month  "))
            c=int(input("year  "))
            break
        except:
            print("error")
    s=date(a,b,c)
    print(s)
    x=input("type 'stop' to exit or enter to continue  ").upper()



