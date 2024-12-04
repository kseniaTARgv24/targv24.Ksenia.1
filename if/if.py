
import random

#from curses.ascii import isalpha 

# print("\n Ul.1\n")
# nimi = input("Mis on sinu nimi")
# if nimi.isalpha() and nimi.isupper():
#      if nimi=="JUKU":
#            print("Lähme kinno")  
#            try:
#                vanus=int(input(f"kui vana sa oled {nimi}"))
#                if vanus<0:
#                    print("viga")
#                elif vanus<=6:
#                    print("tasuta")
#                elif vanus<15:
#                    print("Lastepilet")
#                elif vanus<65:
#                    print("täispilet")
#                elif vanus<100:
#                    print("sooduspilet")
#                else:
#                    print("You're still alive?????")
#            except:
#                print("vale andmetüüb")
#      else:
#            print("Ootan Juku")
# else:
#     print("segatud tähed")

# print("\n Ul.2\n")
# nimi1=("sisesta esimene nimi")
# nimi2=("sisesta teine nimi")
# # 1 var
# nimed=["Kirill","Gleb"]
# if nimi1.isalpha() and nimi2.isalpha():
#      if (nimi1 in nimed) and (nimi2 in nimed):
#          print("Nad on naabrid")
#      else:
#         print("ei ole naabrid")
# else:
#      print(">:(")




# print("\n Ul.3\n")
# print("Anna mulle toa seinade pikkused m")
# try:
#   a=float(input())
#   b=float(input())
# except:
#     print("numbrid!!!")

# S=a*b
# print(f"Pindala on {S} m2")

# vastus=(input("Kas sa tahad teha remondi, jah, ei?"))

# if vastus.upper()=="JAH":
#    print("siis ütle mulle kui palju maksab ruutmeeter euros")
#    hind=float(input())
#    result=S*hind
#    print(f"põranda vahetamise hind on {result}")
# elif vastus.upper()=="EI":
#    print("Nu na net i suda net")
# else:
#  print(r"""
#   /\_/\  
#  ( o.o ) 
#   > ^ <
#   meow""")
#  print(r"""
#   /\     /\
#  {  `---'  }
#  {  O   O  }
#  ~~>  V  <~~
#   \  \|/  /
#    `-----'____
#   /     \    \_
#  {       }\  )_\_   _
#   |  \_/  ) / /   \_/ \
#    \__/  /(_/      \__/
#     (__/
#  """)

# print("\n Ul.4\n")
# try:
#      a=float(input("milline on alghing euros "))
# except:
#      print("Numbers!!")
    
# if a>700:
#      a=a-(a*0.3)
#      print(f"Sul on soodustus! {a:2f} eur")
# else:
#      print("Sul ei ole soodustus.")
#      print(r"""
#      /\_/\  
#    ( ° w ° )
#     (  -  ) 
#     |    |  \
#    (_)(_) (_)
#   """)


# print("\n Ul.5\n")
# t=float(input("Milline on temperatuur sinu toas  "))
# if t< 18.0:
#     print("On liiga külm. on vaja 18")
# elif t == 18.0:
#     print("on ok")
# else:
#     print("on liiga soe. on vaja 18")


# print("\n Ul.6\n")
# p=float(input("Ütle kui pikk sa oled cm"))
# if p < 160:
#     print("Oled väike väike")
#     print(r"""
#       /\_/\  
#      ( o.o ) 
#       > ^ <
#      meow""")
# elif p <= 170:
#     print("oled väga ok")
# else:
#     print("olen suur suur")
#     print(r"""
#      /\     /\
#     {  `---'  }
#     {  O   O  }
#     ~~>  V  <~~
#      \  \|/  /
#       `-----'____
#      /     \    \_
#     {       }\  )_\_   _
#      |  \_/  ) / /   \_/ \
#       \__/  /(_/      \__/
#        (__/
# """)



print("\n Ul.7\n")
p=float(input("Ütle kui pikk sa oled cm"))
s=input("Mis on sinu sugu? (n, m)")

if s.upper()=="N":
    if p<=155:
        print("oled lühike")
    elif p<=175:
        print("oled ok")
    else:
        print("oled pikk")
elif s.upper()=="M":
    if p<=165:
        print("oled lühike")
    elif p<=185:
        print("oled ok")
    else:
        print("oled pikk") 
else:
    print("vasta normaalselt")


print("\n Ul.8\n")
p=input("Kas sa tahad osta piima (jah, ei)")
l=input("Kas sa tahad osta leiba (jah, ei)")
m=input("Kas sa tahad osta munade pakki (jah, ei)")

phind=random_float(1.5, 2.5)
lhind=random_float(1.5, 3.5)
mhind=random_float(2.5, 5.5)

if p.upper()="JAH":

