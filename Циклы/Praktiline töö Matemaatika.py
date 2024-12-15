import random

# operations=["+","-","*","**","/"]
# o=random.choise(operations)
# a=random.randit()
# b=random.randit()                   -шаблон




while True:
    lvl=input("Проверим ваши знания по математике. Выберите уровень сложности (1,2,3): ")
    levels=["1", "2", "3"]
    points = 0
################################################################lvl1
    if lvl.isdigit() and lvl in levels:
        print("Решаем 10 примеров! (При дробном ответе, округли его до 2х знаков после запятой)")
        if lvl == "1":
            for i in range(0,9,1):
                operations=["+","-"]
                o=random.choice(operations)
                a=random.randint(0,10)
                b=random.randint(0,10)
                yourAns=float(input(f"{a}{o}{b} = "))
                if o == "+":
                    ans=a+b
                    ans=float(ans)
                    if ans==yourAns:
                        points+=1
                        print(f"Points: {points}")
                    else:
                         print(f"Points: {points}")
                else:
                    ans=a-b
                    ans=float(ans)
                    if ans==yourAns:
                        points+=1
                        print(f"Points: {points}")
                    else:
                         print(f"Points: {points}")
            if points <6:
                print("оценка 2")
            elif points < 80:
                print("оценка 3")
            elif points < 90:
                print("оценка 4")
            else:
                print("оценка 5")
############################################################lvl2
        if lvl == "2":
            for i in range(0,9,1):
                operations=["+","-","*","/"]
                o=random.choice(operations)
                a=random.randint(0,100)
                b=random.randint(0,100)
                yourAns=float(input(f"{a}{o}{b} = "))
                if o == "+":
                    ans=a+b
                    ans=float(ans)
                    if ans==yourAns:
                        points+=1
                        print(f"Points: {points}")
                    else:
                         print(f"Points: {points}")
                elif o == "-":
                    ans=a-b
                    ans=float(ans)
                    if ans==yourAns:
                        points+=1
                        print(f"Points: {points}")
                    else:
                         print(f"Points: {points}")
                elif o == "*":
                    ans=a*b
                    ans=float(ans)
                    ans=round(ans,2)
                    if ans==yourAns:
                        points+=1
                        print(f"Points: {points}")
                    else:
                         print(f"Points: {points}")
                elif o == "/":
                    ans=a/b
                    ans=float(ans)
                    ans=round(ans,2)
                    if ans==yourAns:
                        points+=1
                        print(f"Points: {points}")
                    else:
                         print(f"Points: {points}")
            if points <6:
                print("оценка 2")
            elif points < 80:
                print("оценка 3")
            elif points < 90:
                print("оценка 4")
            else:
                print("оценка 5")
###########################################################lvl3
        if lvl == "3":
            for i in range(0,9,1):
                operations=["*","/","**"]
                o=random.choice(operations)
                a=random.randint(0,100)
                b=random.randint(0,100)
                yourAns=float(input(f"{a}{o}{b} = "))
                if o == "*":
                    ans=a*b
                    ans=float(ans)
                    ans=round(ans,2)
                    if ans==yourAns:
                        points+=1
                        print(f"Points: {points}")
                    else:
                         print(f"Points: {points}")
                elif o == "/":
                    ans=a/b
                    ans=float(ans)
                    ans=round(ans,2)
                    if ans==yourAns:
                        points+=1
                        print(f"Points: {points}")
                    else:
                         print(f"Points: {points}")
                elif o == "**":
                    ans=a**b
                    ans=float(ans)
                    ans=round(ans,2)
                    if ans==yourAns:
                        points+=1
                        print(f"Points: {points}")
                    else:
                         print(f"Points: {points}")
            if points <6:
                print("оценка 2")
            elif points < 80:
                print("оценка 3")
            elif points < 90:
                print("оценка 4")
            else:
                print("оценка 5")
        break
    else:
        print("Неверный уровень")



 

         

          

        


