


def kontrollnumber(ik)->int:
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
    return kn


def result(ik)->str:

    if ik[0] == "1":
        v=(ik + " - male," + ik[5:7] + "." + ik[3:5] + ".18" + ik[1:3])
    elif ik[0] == "2":
        v=(ik + " - female," + ik[5:7] + "." + ik[3:5] + ".18" + ik[1:3])
    elif ik[0] == "3":
        v=(ik + " - male," + ik[5:7] + "." + ik[3:5] + ".19" + ik[1:3])
    elif ik[0] == "4":
        v=(ik + " - female," + ik[5:7] + "." + ik[3:5] + ".19" + ik[1:3])
    elif ik[0] == "5":
        v=(ik + " - male," + ik[5:7] + "." + ik[3:5] + ".20" + ik[1:3])
    elif ik[0] == "6":
        v=(ik + " - female," + ik[5:7] + "." + ik[3:5] + ".20" + ik[1:3])

    return v

def haigla(ik)->str:
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
        return a
    elif n >= 11 and n <= 19:
        return b
    elif n >= 21 and n <= 220:
        return c
    elif n >= 221 and n <= 270:
        return d
    elif n >= 271 and n <= 370:
        return e
    elif n >= 371 and n <= 420:
        return f
    elif n >= 421 and n <= 470:
        return g
    elif n >= 471 and n <= 490:
        return h
    elif n >= 491 and n <= 520:
        return i
    elif n >= 521 and n <= 570:
        return j
    elif n >= 571 and n <= 600:
        return k
    elif n >= 601 and n <= 650:
        return l
    elif n >= 651 and n <= 700:
        return m
