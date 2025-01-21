# Проверка личного кода
# Безконечно запрашиваем личные коды.
# Проверяем их:
# - если 11 символов/чисел, то продолжаем проверку, если нет, то сообщить, что кол-во цифт не верное и запрашивает новый личный код,
# Первый символ только:1,2,3,4,5,6, если числа другие, то прерываем проверку и запрашиваем новый личный код,
# Второй-седьмой символы- должны сообветствовать цифрам дат рождения, если нет, то новый личный код,
# Найти контрольный номер (смотри ниже пояснение)
# * Если личный код правильный, то добавить его в список ikoodid, а на экран вывести фразу:
# Это {пол}, его/ее день рождения {дата рождения}  и место рождения {название города и больницы}
# * Если код не верный, то он добавляется в список arvud

# После прерывания бесконечного цикла проверки, надо вывести на экран оба списка (ikoodid, arvud).
# Список arvud упорядочи по-возростанию, список ikoodid отобрази таким образом, что сначала личные коды женщин, потом мужчин.
# Способ остановки цикла придумай сам.

# Например: Если личный код 47610112243, то будет след. фраза: Это женцина, его/ее день рождения 11.10.1976  и место рождения Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi).

# Пол 1,3,5 -муж, 2,4,6-жен

#60107150237

print("IKOOD\n")

ikoodid=[]
arvud=[]
stop=" "

while stop != "STOP":
    ik=input("Enter ikood: ")
    while len(ik)!=11 or not ik.isdigit():
        arvud.append(ik)
        ik=input("Your ikood has wrong number of symbols or contains letters! Enter ikood again (11 symbols and only numbers): ")
    while ik[0] not in ["1","2","3","4","5","6"]:
        arvud.append(ik)
        ik=input("The ikood must start with 1,2,3,4,5 or 6! Enter ik again: ")
    while True:
        if 0<=int(ik[1:3])<=99 and 1<=int(ik[3:5])<=12 and 1<=int(ik[5:7])<=31:
            break
        else :
            arvud.append(ik)
            ik = input("the 2-7 symbols cannot be date of birth. Enter ikood again: ")
    #Контрольное число
    # Вес первой степени: 1 2 3 4 5 6 7 8 9 1
    # Вес второй степени: 3 4 5 6 7 8 9 1 2 3



    kaal1=[1,2,3,4,5,6,7,8,9,1]
    kaal2=[3,4,5,6,7,8,9,1,2,3]
    summ=0

    for i in range(10):
        mult=int(ik[i])*kaal1[i]
        summ+=mult
    if summ%11 == 10:
        for i in range(10):
            mult=int(ik[i])*kaal2[i]
            summ+=mult 
        if summ%11 == 10:
            kn = 0
        else:
            kn=summ%11
    else:
        kn=summ%11
     
    if int(ik[10]) == kn:
        print("ikood is right!(kontrollnumber matches)\n\n")
        ikoodid.append(ik)

        if ik[0] == "1":
            print(ik + " - male," + ik[5:7] + "." + ik[3:5] + ".18" + ik[1:3])
        elif ik[0] == "2":
            print(ik + " - female," + ik[5:7] + "." + ik[3:5] + ".18" + ik[1:3])
        elif ik[0] == "3":
            print(ik + " - male," + ik[5:7] + "." + ik[3:5] + ".19" + ik[1:3])
        elif ik[0] == "4":
            print(ik + " - female," + ik[5:7] + "." + ik[3:5] + ".19" + ik[1:3])
        elif ik[0] == "5":
            print(ik + " - male," + ik[5:7] + "." + ik[3:5] + ".20" + ik[1:3])
        elif ik[0] == "6":
            print(ik + " - female," + ik[5:7] + "." + ik[3:5] + ".20" + ik[1:3])

        a = ["Kuressaare Haigla"]
        b = ["Tartu Ülikooli Naistekliinik", "Tartumaa", "Tartu"]
        c = ["Ida-Tallinna Keskhaigla", "Pelgulinna sünnitusmaja", "Hiiumaa", "Keila", "Rapla haigla", "Loksa haigla"]
        d = ["Ida-Viru Keskhaigla", "Kohtla-Järve", "endine Jõhvi"]
        e = ["Maarjamõisa Kliinikum", "Tartu", "Jõgeva Haigla"]
        f = ["Narva Haigla"]
        g = ["Pärnu Haigla"]
        h = ["Pelgulinna Sünnitusmaja", "Tallinn", "Haapsalu haigla"]
        i = ["Järvamaa Haigla", "Paide"]
        j = ["Rakvere", "Tapa haigla"]
        k = ["Valga Haigla"]
        l = ["Viljandi Haigla"]
        m = ["Lõuna-Eesti Haigla", "Võru", "Põlva Haigla"]

        n=int(ik[7:9])
        if n >= 1 and n <= 10:
            print(a)
        elif n >= 11 and n <= 19:
            print(b)
        elif n >= 21 and n <= 220:
            print(c)
        elif n >= 221 and n <= 270:
            print(d)
        elif n >= 271 and n <= 370:
            print(e)
        elif n >= 371 and n <= 420:
            print(f)
        elif n >= 421 and n <= 470:
            print(g)
        elif n >= 471 and n <= 490:
            print(h)
        elif n >= 491 and n <= 520:
            print(i)
        elif n >= 521 and n <= 570:
            print(j)
        elif n >= 571 and n <= 600:
            print(k)
        elif n >= 601 and n <= 650:
            print(l)
        elif n >= 651 and n <= 700:
            print(m)
        print("\n\n")

    else:
        print("ikood is wrong... (kontrollnumber doesnt match)")
        arvud.append(ik)
 
    print("All entered ikoods:\n",ikoodid)
    print("All wrong attemts:\n",arvud)
    stop=input("\n\nEnter <<stop>>, if you want to finish. Or press enter to continue--> ").upper()







#     Haiglatele eraldatud järjekorranumbri vahemikud arvatakse olevat üldjoontes järgmised:

# 001...010 = Kuressaare Haigla

# 011...019 = Tartu Ülikooli Naistekliinik, Tartumaa, Tartu
# 021...220 = Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla
# 221...270 = Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)
# 271...370 = Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla
# 371...420 = Narva Haigla
# 421...470 = Pärnu Haigla
# 471...490 = Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla
# 491...520 = Järvamaa Haigla (Paide)
# 521...570 = Rakvere, Tapa haigla
# 571...600 = Valga Haigla
# 601...650 = Viljandi Haigla
# 651...700? = Lõuna-Eesti Haigla (Võru), Põlva Haigla

        