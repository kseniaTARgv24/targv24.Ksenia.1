
print("------------Reference classwork--------------\n")
spisok=[]
numbers=[1,2,3,4,5]
abc=['a','b','ccc']
slovo='programmirovanie'
slovo_list=list(slovo)
print(slovo)
print(slovo_list)

a = 1000000

while a != 0:
    print("1- add letter to the list")
    print("2 - merge lists")
    print("3 - insert letter ")
    print("4 - remove element")
    print("0 - to finish")

    a=int(input())
    if a == 1:
        slovo_list.append(input("input a letter  "))
        print(slovo_list)
    elif a == 2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif a  == 3:
        a = input("insert letter ")
        i=int(input("give the number of its position  "))
        slovo_list.insert(i-1,a)
        print(slovo_list)
    elif a ==4:
        a=input("give an element you want to remove")
        if a not in slovo_list:
            print("nothing to delete")
        else:
            while slovo_list.count(a) != 0:
                slovo_list.remove(a)
            print(slovo_list)


print("\n\n------------Independent work-------------------- \n")
print("""
      ref.1 
  work with lists

    """)

a=""
casher=""
while True:

    products=['milk','very sharp knife','rat poison','catnip cigarettes']
    product_index=[3,5,5,3]
    product_dict = dict(zip(products, product_index)) #использую словарь, чтобы приписать "цены" (индексы) из одного списка к "товарам" из другого списка
    bag=[]
    wallet = 8 

    print(product_dict)

    print("WelCOmE Tto ouR SHopp. Chhose pProduCTs oror LeaVVE!*!!")
    a=input("you: I-i will (shop/leave)... ").upper()

    if a not in ['SHOP', 'LEAVE']:
        i=0
        while True:                                               #Цикл, работающий пока пользователь не введет корректный ответ, или пока не закончатся попытки   
            if i < 2:
                print("WhaT aree You MMumbling there, MmouSkin??")
                a=input("you: I-i will (shop/leave)... ").lower()
                if a not in ['shop','leave']:
                    i+=1
                    # print(i)
                else:
                    a = "LEAVE"
                    break
            else :
                print("OHH GET OUT YOU ANNOYING STINKY RAT. GET BACK WHEN YOU'RE ABLE TO SPPEAAK")
                casher="angry"
                a = "LEAVE"
                break
            
    if a =="LEAVE":   #проверка условия цикла в середине цикла, чтобы при необходимости его прервать
        break

    print("GGOOD AHA! Take WhAt yOu Like.....")
    while True:
        if wallet>= min(product_index):
            print(product_dict)
            print("*You scanning the counter in silence. What will you buy? Remember! you have ",wallet," coins in your wallet!*")
            buy=input().lower()         #пользователь вводит название товара, все буквы переводятся в нижний регистр
            if buy in product_dict:              #если товар правильный, те если такой есть в списке....
                find_index=product_dict[buy]     # находим "цену" или индекс, соответствующий товару в списке "словаря"
                products.remove(buy)             # убираем "купленный" товар из списка товаров
                product_index.remove(find_index) # убираем соответствующий индекс, который нашли ранее 
                product_dict = dict(zip(products, product_index)) #состовляем "словарь" заново с обновленными списками

                bag.append(buy)                 # добавляем "купленные" товары в "сумку"

                wallet-=find_index              # из "денег" вычитаем значение найденного ранее индекса, те "цену" товара
                print("*The coins with a jingling sound fell onto the counter.*")
                print("*",wallet," coins left in your wallet*")
                print("*You have ",bag," in your bag now*")

            else:
                print("ARE YOU SCHIZO, MY MOUSEKIN??? THERE IS NO SUCH PRODUCT!")
        else:
            print("HeheH. LOoKs lIkE SOMeoNe rAn OUt off mooNey")
            break


    break
          
        

if casher == "angry":
    print("*You flee with embaressment and never come back to this shop*")
else:
    print("Wwell, MmoUsKin, seee yOu laTter... HHopefullY, a-l-i-v-e...\n\n")

    if 'milk' in bag and 'very sharp knife' in bag:
        print("You carry your bag with ", bag, " with relief. You slightly regret grabbing the milk out of fear of the cashier. But you're glad he didn't suspect anything. Maybe you'll even like the taste of milk? Especially if you add a little iron to it...")
    elif 'milk' in bag and 'catnip cigarettes' in bag:
        print("As you walk with your bag, ", bag, ", a strange mix of curiosity and guilt nags at you. Milk and catnip cigarettes? Perhaps tonight you'll discover just how creative your dreams can get.")
    elif 'rat poison' in bag and 'catnip cigarettes' in bag:
        print("Your bag with ", bag, " feels heavier with intent. Poison and catnip? Perhaps it's not just the rats who'll lose themselves tonight.")


print("\nthe end\n\n")

print("""
      ref.2 
  other functions

    """)
print("Replacing a pattern S.replace(pattern, replacement)")
text = "I have a cat."
print("Original:", text)
print(text.replace("cat", "dog"))
print("")

print("Splitting a string by a delimiter S.split(symbol)")
text = "milk bread cheese"
print("Original:", text)
print(text.split(" "))
print("")
print("Is the string made of digits? S.isdigit()")
text = "12345"
print("Original:", text)
print(text.isdigit())
print("")
print("Is the string made of letters? S.isalpha()")
text = "hello"
print("Original:", text)
print(text.isalpha())
print("")
print("Is the string made of digits or letters? S.isalnum()")
text = "hello123"
print("Original:", text)
print(text.isalnum())
print("")
print("Is the string in lowercase? S.islower()")
text = "hello"
print("Original:", text)
print(text.islower())
print("")
print("Is the string in uppercase? S.isupper()")
text = "HELLO"
print("Original:", text)
print(text.isupper())
print("")
print("Does the string contain only whitespace characters? S.isspace()")
text = "   "
print("Original:", text)
print(text.isspace())
print("")
print("Do words in the string start with uppercase letters? S.istitle()")
text = "Hello World"
print("Original:", text)
print(text.istitle())
print("")
print("Convert the string to uppercase S.upper()")
text = "hello"
print("Original:", text)
print(text.upper())
