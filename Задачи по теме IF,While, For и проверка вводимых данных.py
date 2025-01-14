# 0. Программу написаную на уроке по блок схемам: https://moodle.edu.ee/mod/assign/view.php?id=469362 прикрепите как ответ на задание.

# 1. Определить и вывести максимальное из N вводимых пользователем чисел.

# 2. Написать программу, которая бы запрашивала целые числа и распечатывала любые значение, кроме13. Если заданное число равно13, вместо него печатается число 77.

# 3. Начав тренировки, спортсмен в первый день пробежал 10 км. Каждый день он увеличивал дневную норму на 10% нормы предыдущего дня. Какой суммарный путь пробежит спортсмен за 7 дней?

# 4. Имеется кусок ткани длиной М метров. От него последовательно отрезаются куски разной длины. Все данные по использованию ткани заносятся в компьютер. Компьютер должен выдать сообщение о том, что материала не хватает, если будет затребован кусок ткани, большей длины, чем имеется и предложить выкупить остаток. Если пользователь согласен, то продается последний кусок и программа заканчивает работу, если нет, то переходим к следующиму покупателю.

# 5. Составьте программу для вычисления площади трапеций до тех пор пока пользователь не откажется вычислать.

# 6. Составьте программу, проверяющую, верно ли утверждение, что введенное вами целое число делится без остатка на 3.

#########

print("\n\nn.1\n")
N=int(input("How many numbers will be input? - "))
list=[]
print("start:")

for i in range(0,N,1):
    while True:
        try:
            user_input = input(f"{i+1} number is: ")
            user_input = float(user_input)
            list.append(user_input)
            break

        except:
            print("please, input correct number")
maximum= max(list)
print(f"max num is {maximum}")

#############

print("\n\nn.2\n")
while1 = True
while while1:
    try:
        a=input("Give me a whole number and i will print it out: ")
        a = int(a)
        if a == 13:
            print("77 (oops)")
        else:
            print(a)
        
        while2 = True
        while while2:
            b=input("wanna try again?(y/n)")
            b=b.upper()
            while2 = True
            if b == "N" or b=="NO":
                while1 = False
                while2 = False
            elif b == "Y" or b == "YES":
                while2 = False
            else:
                print("wrong input")
    except ValueError: 
        print("I said, whole number!")

#################

print("\n\nn.3\n")
print("Начав тренировки, спортсмен в первый день пробежал 10 км. Каждый день он увеличивал дневную норму на 10% нормы предыдущего дня. Какой суммарный путь пробежит спортсмен за 7")
a=10
days=7

for i in range(0,days,1):
    a=a+a*0.1

print(f"\nThe answer is {round(a,2)} km")

print("\nTry imput your own numbers!")
a=input("Distance in the 1st day: ")
days=input("How many days in total: ")
while True:
    try:
        a = float(a)
        days = int(days)
        for i in range(0,days,1):
            a=a+a*0.1
        break
    except ValueError:
        print("wrong numbers")

print(f"\nThe answer is {round(a,2)} km")

#####################

print("\n\nn.4\n")
print("PS. try to mess around with the inputs!!!!!!")
while True:
    try:
        roll= float(input("Youre working at the fabric shop! Lets assume you have the roll of fabric. How many meters do you have there? --> "))
        break
    except ValueError:
        print("invalid input")
i=1
while roll != 0:
    try:
        cut=float(input(f"The {i} customer is here! How much of the fabric do they want? -->"))
        if cut<=roll:
            roll = roll-cut
            enter=input(f"Sold! You have {roll} m left in a roll (press enter to continue)")
            i+=1
        elif cut>roll:
            print(f"Oh... There is not enough in the roll - {roll}m... Ask them if they want to buy leftover anyway. ")
            answer=input("Do they want?(y/n)").upper()

            if answer in ["Y","YES"]:
                    while True:
                        try:
                            cut=float(input(f"How much of the leftover fabric do they want? -->"))

                            while cut>roll:
                                print("No, the customer should pick an available quantity! Again...")
                                cut=float(input(f"How much of the leftover fabric do they want? -->"))

                            roll = roll-cut
                            i =+ 1
                            enter=input(f"Sold! You have {roll} m left in a roll (press enter to continue)")
                            break
                        except ValueError:
                            print("invalid input")
            elif answer in ["N", "NO"]:
                    enter=input(("Well, maybe another customer will buy the leftover... (press enter to continue)"))
                    i+=1
            else:
                    print("Wrong input. Lets try again")
    except ValueError:
        print("invalid input")

print("No fabric left! Sold out!")

#######################

print("\n\nn.5\n")
print("let's calculate the area of ​​a trapezium! If you're tired and want to finish, just write STOP")
print(" The firmula of area of trapezium is 1/2 * (a + b) * h")
user_input="user_input"
while user_input != "STOP":
    while True:
        try:
            a=float(input("a = "))
            b=float(input("b = "))
            h=float(input("h = "))
            break
        except ValueError:
            print("wrong input!")
    
    S = 1/2 * (a + b) * h
    print(f"The area of trapezium is {S}")
    user_input=input("").upper()

###########################

print("\n\nn.6\n")
user_input=" "
print("Give a number and I will tell you whether it is divisible by 3 without a remainder. If you're tired and want to finish, just write STOP")
while user_input != "STOP":
    while True:
        try:
            a=float(input("number = "))
            break
        except ValueError:
            print("wrong input!")
    if a%3 != 0:
        b = a%3
        print(f"You get a remainder -  {b} from {a} / 3 = {round(a/3)}")
        user_input=input().upper()
    else:
        print(f"There is no remainder! a / 3 = {a/3}")
        user_input=input().upper()








