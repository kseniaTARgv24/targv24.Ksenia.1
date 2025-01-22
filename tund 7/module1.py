from re import S
from xmlrpc.client import boolean


def summa3(arv1:int,arv2:int,arv3:int)->int:
    """

    :param int arv1: Esimene n:
    :param int arv2: Teine n:
    :param int arv3: Kolmas n:
    :rtype: int

    """

    summa = arv1+arv2+arv3
    return summa

def arithmetic(a:float,b:float,c:str)->float:
    if c == "+":
        s=a+b
    elif c == "-":
        s=a-b
    elif c == "*":
        s=a*b
    elif c == "/":
        s=a/b
    else:
        s = str("ERROR")
    return s


def is_year_leap(a:int)->bool:
        if a%4==0:
            s=True
        else:
            s=False
        return s

def square(a:float)->float:
    S=a*a
    P=a*4
    d=2**(1/2)*a
    return S,P,d

def season(a:int)->str:
    if a in [12,1,2]:
        s="winter"
    elif a in [3,4,5]:
        s="spring"
    elif a in [6,7,8]:
        s="summer"
    elif a in [9,10,11]:
        s="fall"
    else:
        s="error"
    return  s

def bank(a:float,years:int)->float:
    for i in range (1,years,1):
        a+=a*0.1
    return a

def is_prime(a:float)->bool:
    if a > 1:
        if a%2 == 0 or a%3==0:
            s=False
        else:
            s=True
    else:
        s= False
    return s
        



def date(a:int,b:int,c:int)->bool:
    if 0<a<32 and 0<b<13 and 0<c:
        if a == 31 and b in [1,12,10,8,7,5,3]:
            v=True
        elif a == 30 and b in [11,9,6,4]:
            v=True
        elif a ==28 and b == 3 and c%4!=0:
            v=True
        elif a ==29 and b == 3 and c%4==0:
            v=True
        else:
            v=False
    else:
        v=False
    return v

def XOR_cipher(a:str, key:str)->str:
    coded=" "
    for symbol in text:
        coded+=chr(ord(symbol)^key)
    return coded



