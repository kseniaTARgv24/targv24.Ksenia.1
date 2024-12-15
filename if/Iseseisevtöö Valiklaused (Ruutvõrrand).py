



print("\n\n1.\n")
a=float(input("Введите число:\n"))
if a>0:
    print("Число положительное")    
    b=a%2
    if b == 0:
        print("Число чётное")
    else:
        print("Число нечётное")
else:
     print("Число отрицательное")


print("\n\n2.\n")
print("Введите 3 числа и программа проверит, могут ли они являться углами треугольника")
a=float(input())
b=float(input())
c=float(input())

if a>0 and b>0 and c>0:
        if a+b+c==180:
                print("Числа могут быть углами треугольника.")
                if a==b or b==c or a==c:
                    print("Треугольник равнобедренный")
                elif a==b==c:
                    print("Треугольник равносторонний")
                else:
                    print("Треугольник разносторонний")
        else:
                print("Одно или более чисел отрицательны и не могут быть углами треугольника")


print("\n\n3.\n")
a=input("Хотите расшифровать порядковый номер дня недели в название?\n")
if a.upper()=="да" or a.upper()=="jah" or a.upper()=="yes":
        b=int(input("Введите номер дня недели\n"))
        if b == 1:
          print("Понедельник")
        elif b == 2:
          print("Вторник")
        elif b == 3:
          print("Среда")
        elif b == 4:
          print("Четверг")
        elif b == 5:
          print("Пятница")
        elif b == 6:
          print("Суббота")
        elif b == 7:
          print("Воскресенье")
        else:
            print("Нет, нужно от 1 до 7")

print("\n\n4.\n")
print("назоваите дату своего рождения и программа определит ваш знак зодиака.")
a=input("месяц словами: ").lower()
b=input("день: ")
months = ["январь", "февраль", "март", "апрель", "май", 
          "июнь", "июль", "август", "сентябрь", "октябрь", 
          "ноябрь", "декабрь"]

if b.isdigit() and a in months:
    b = int(b)
    if (a == "январь" and 0 < b < 20) or (a == "декабрь" and 31 > b >= 22):
        print("Козерог")
    elif (a == "январь" and 20 <= b <= 31) or (a == "февраль" and 0 < b < 19):
        print("Водолей")
    elif (a == "февраль" and 19 <= b <= 29) or (a == "март" and 0 < b < 21):
        print("Рыбы")
    elif (a == "март" and 21 <= b <= 31) or (a == "апрель" and 0 < b < 20):
        print("Овен")
    elif (a == "апрель" and 20 <= b <= 30) or (a == "май" and 0 < b < 21):
        print("Телец")
    elif (a == "май" and 21 <= b <= 31) or (a == "июнь" and 0 < b < 21):
        print("Близнецы")
    elif (a == "июнь" and 21 <= b <= 30) or (a == "июль" and 0 < b < 23):
        print("Рак")
    elif (a == "июль" and 23 <= b <= 31) or (a == "август" and 0 < b < 23):
        print("Лев")
    elif (a == "август" and 23 <= b <= 31) or (a == "сентябрь" and 0 < b < 23):
        print("Дева")
    elif (a == "сентябрь" and 23 <= b <= 30) or (a == "октябрь" and 0 < b < 23):
        print("Весы")
    elif (a == "октябрь" and 23 <= b <= 31) or (a == "ноябрь" and 0 < b < 22):
        print("Скорпион")
    elif (a == "ноябрь" and 22 <= b <= 30) or (a == "декабрь" and 0 < b < 22):
        print("Стрелец")




# if b.isdigit():
#     b =int(b)
#     a =str(a)
#     if a == "1" or a.upper()== "январь":
#         if 0<b<20:
#             print("Козерог")
#         elif b>=20:
#             print("Водолей")
#     elif a == "2" or a.upper()== "февраль":
#         if 0<b<19:
#             print("Водолей")
#         elif b>=19:
#             print("Рыбы")
#     elif a == "3" or a.upper()== "март":
#         if 0<b<21:
#             print("Рыбы")
#         elif b>=21:
#             print("Овен")
#     elif a == "4" or a.upper()== "апрель":
#         if 0<b<20:
#             print("Овен")
#         elif b>=20:
#             print("Телец")
#     elif a == "5" or a.upper()== "май":
#         if 0<b<21:
#             print("Телец")
#         elif b>=21:
#             print("Близнецы")
#     elif a == "6" or a.upper()== "июнь":
#         if 0<b<21:
#             print("Близнецы")
#         elif b>=21:
#             print("Рак")
#     elif a == "7" or a.upper()== "июль":
#         if 0<b<23:
#             print("Рак")
#         elif b>=23:
#             print("Лев")
#     elif a == "8" or a.upper()== "август":
#         if 0<b<23:
#             print("Лев")
#         elif b>=23:
#             print("Дева")
#     elif a == "9" or a.upper()== "сентябрь":
#         if 0<b<23:
#             print("Дева")
#         elif b>=23:
#             print("Весы")
#     elif a == "10" or a.upper()== "октябрь":
#         if 0<b<23:
#             print("Весы")
#         elif b>=23:
#             print("Скорпион")
#     elif a == "11" or a.upper()== "ноябрь":
#         if 0<b<22:
#             print("Скорпион")
#         elif b>=22:
#             print("Стрелец")
#     elif a == "12" or a.upper()== "декабрь":
#         if 0<b<22:
#             print("Стрелец")
#         elif b>=22:
#             print("Козерог")
# else:
#     print("Неверные данные")


print("\n\n5.\n")
a=input("Введите число: ")
try:
    a=float(a)
    if a.is_integer():
        a50=a*0.5
        print(f"50% от числа {a50}")
    else:
        a70=a*0.7
        print(f"70% от числа {a70:.2f}")
except:
        print(f"Это текст: {a}")


print("\n\n6.\n")

Y=input("Решим квадратное уравнение?").lower()
if Y == "да":
    print("Введите 3 числа")
    a=input()
    b=input()
    c=input()
    try:
        a=float(a)
        b=float(b)
        c=float(c)
        D=b**2-4*a*c
        print(f"Находим D: D=b**2-4ac --> D= {D}")
        if D>0:
            x1=(-b+D**(-2))/(2*a)
            x2=(-b-D**(-2))/(2*a)
            print(f"Два решения: х1 = {x1:.2f} , х2 = {x2:.2f}")
        elif D==0:
           x=(-b)/(2*a)
           print(f"Одно решение: х = {x:.2f}")
        else:
           print("Решений нет")
    except:
        print("Неверные данные")
elif Y == "нет":
    print("Ну на нет и суда нет")
else:
    print("да или нет?")




