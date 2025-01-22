#~_~
from module1 import *

# a=int(input("a = "))
# b=int(input("b = "))
# c=int(input("c = "))
# S=summa3(a,b,c)
# print(S)

# a=float(input("a = "))
# b=float(input("b = "))
# c=input("operation = ")
# S=arithmetic(a,b,c)
# print(S)



# while True:
#     try:
#         year = int(input("year: "))
#         break
#     except:
#         print("error")
# S=is_year_leap(year)
# print(S)

# a=float(input("a = "))
# V=square(a)
# print(V)

# a=int(input("month = "))
# s=season(a)
# print(s)

# a=float(input("вклад = "))
# years=int(input("период (года) = "))
# s=bank(a,years)
# print(s)


b=" "
while b!="STOP":
    while True:
        try:
            a=float(input("простое ли число? --> "))
            v=is_prime(a)
            print(v)
            break
        except:
            print("error")
    b=input("type 'stop' to exit or enter to continue  ").upper()






a=int(input("day  "))
b=int(input("month  "))
c=int(input("year  "))
s=date(a,b,c)
print(s)



