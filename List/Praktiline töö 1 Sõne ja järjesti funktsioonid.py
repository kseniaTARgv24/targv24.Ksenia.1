

# spisok=[]
# numbers=[1,2,3,4,5]
# abc=['a','b','ccc']
# slovo='programmirovanie'
# slovo_list=list(slovo)
# print(slovo)
# print(slovo_list)

# a = 1000000

# while a != 0:
#     print("1- add letter to the list")
#     print("2 - merge lists")
#     print("3 - insert letter ")
#     print("4 - remove element")
#     print("0 - to finish")

#     a=int(input())
#     if a == 1:
#         slovo_list.append(input("input a letter  "))
#         print(slovo_list)
#     elif a == 2:
#         slovo_list.extend(abc)
#         print(slovo_list)
#     elif a  == 3:
#         a = input("insert letter ")
#         i=int(input("give the number of its position  "))
#         slovo_list.insert(i-1,a)
#         print(slovo_list)
#     elif a ==4:
#         a=input("give an element you want to remove")
#         if a not in slovo_list:
#             print("nothing to delete")
#         else:
#             while slovo_list.count(a) != 0:
#                 slovo_list.remove(a)
#             print(slovo_list)



a=""
casher=""
while True:

    products=['milk','very sharp knife','rat poison','catnip cigarettes']
    product_index=[2,5,3,3]
    product_dict = dict(zip(products, product_index))
    bag=[]
    wallet = 8

    print(product_dict)

    print("WelCOmE Tto ouR SHopp. Chhose pProduCTs oror LeaVVE!*!!")
    a=input("you: I-i will (shop/leave)... ").upper()

    if a not in ['SHOP', 'LEAVE']:
        i=0
        while True:
            if i < 2:
                print("WhaT aree You MMumbling there, MmouSkin??")
                a=input("you: I-i will (shop/leave)... ").lower()
                if a not in ['shop','leave']:
                    i+=1
                    # print(i)
                else:
                    break
            else :
                print("OHH GET OUT YOU ANNOYING STINKY RAT. GET BACK WHEN YOU'RE ABLE TO SPPEAAK")
                casher="angry"
                a = "LEAVE"
                break
            
    if a =="LEAVE":
        break

    print("GGOOD AHA! Take WhAt yOu Like.....")
    b=0
    while b < 2:
        print(product_dict)
        print("*You scanning the counter in silence. What will you buy? Remember! you have ",wallet," coins in your wallet!*")
        buy=input().lower()
        if buy in product_dict:
            find_index=product_dict[buy]
            products.remove(buy)
            product_index.remove(find_index)
            product_dict = dict(zip(products, product_index))

            bag.append(buy)

            wallet-=find_index
            print("*The coins with a jingling sound fell onto the counter.*")
            print("*",wallet," coins left in your wallet*")
            print("*You have ",bag," in your bag now*")
            b+=1

        else:
            print("ARE YOU SCHIZO, MY MOUSEKIN??? THERE IS NO SUCH PRODUCT!")

    break
          
        

if casher == "angry":
    print("*You flee with embaressment and never come back to this shop*")
else:
    print("Wwell, MmoUsKin, seee yOu laTter... HHopefullY, a-l-i-v-e...\n\n")

    if 'milk' in bag and 'very sharp knife' in bag:
        print("You carry your bag with ",bag," with relief. You slightly regret grabbing the milk out of fear of the cashier. But you're glad he didn't suspect anything. Maybe you'll even like the taste of milk? Especially if you add a little iron to it...")


