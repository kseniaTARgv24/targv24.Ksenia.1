print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
        a = int(input("Sisestage täisarv => "))  # закрывающие скобки
        break
    except ValueError:
            print("See ei ole täisarv")

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a == 0:  #  двойное равенство (==) 
    print("Nulliga pole mõtet midagi ette võtta")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c = b = a  #  присваивание (=)
    paaris = 0  #  присваивание (=)
    paaritu = 0  # присваивание
    while b > 0:  # двоеточие (:)
        if b % 2 == 0:  #  двойное (==)
            paaris += 1  # =+ на +=
        else:
            paaritu += 1  # =+ на +=
        b = b // 10
    
    print("Paarisarvud:", paaris)  # запятая между строкой и переменной
    print("Paaritud numbrid:", paaritu)  # Аналогично
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake* sisestatud number")
    print()
    b = 0
    while a > 0:  # Добавлено двоеточие (:)
        number = a % 10
        a = a // 10
        b = b * 10
        b += number  #=+ на +=
    print("*Tagurpidi* number", b)  # запятая между строкой и переменной
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Siracuse hüpoteesi testimine")  # лишняя открывающая скобка
    print()
    # if c % 2 == 0:  # двойное (==)
    #     print("с - чётное число. Делим на 2.")
    # else:
    #     print("с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c != 1:
        if c % 2 == 0:  # двойное (==)
            print('{:>4}'.format(round(c)),"- Paris Arv, Jagame 2.")
            c = c / 2  # присваивание (=)
        else:
            c = (3 * c + 1) / 2  # присваивание
            print('{:>4}'.format(round(c)),"- Pariisi arv, korrotame 3, liidate 1 ja zhagame 2.")
        print(c, end=" ")  # кавычка (") и пробел
    print()
    print("Hüpotees on õige")  # лишняя кавычка

