from random import *
import tkinter as tk


def file_to_dict(f: str):
    country_capital = {}  # Dictionary {"Country": "Capital"}
    capital_country = {}  # Dictionary {"Capital": "Country"}
    countries = []  # List to store country names
    capitals = []

    file = open(f, 'r', encoding="utf-8-sig")  # Open file with utf-8-sig encoding
    for line in file:
        k, v = line.strip().split('-', 1)  # Split each line by '-'
        country_capital[k] = v  # Fill country_capital dictionary
        capital_country[v] = k  # Fill capital_country dictionary
        countries.append(k)  # Append the country name to countries list
        capitals.append(v)
    file.close()
    return country_capital, capital_country, countries, capitals  # Return the dictionaries and list

# Call the function and assign the result to variables
country_capital, capital_country, countries, capitals = file_to_dict("riigid_pealinnad.txt")






# mainscreen = tk.Tk()
# mainscreen.title("Europe")
# mainscreen.geometry("400x400")

# tk.Label(mainscreen, text = "Europe").pack(pady=20)


# my_menu = tk.Menu(mainscreen)
# mainscreen.config(menu = my_menu)

# v_menu= tk.Menu(my_menu, tearoff = 0)
# my_menu.add_cascade(label="Find country by capital", menu = v_menu)





print("Menu: \n\n1 -- Find country by capital \n\n2 -- Find capital by country\n\n3 -- Try your knowledge!\n\n0 -- QUIT")
while True:
    action = int(input("\n\n Insert the number of the wanted action --> "))
    if action in [0, 1, 2, 3]:


        ###################### MENU ACTIONS
        if action == 0:
            break


        elif action == 1:
            while True:
                capital = input("Capital (in Estonian): ").capitalize()
                if capital in capitals :
                    print("Country: ", capital_country[capital])
                    ans= input("\nFound a mistake in a country name? (y/n)").lower()
                    if ans=="y":
                        del capital_country[capital]
                        country=input("Please write the right name of a country (in Estonian) --> ")
                        capital_country[capital]=country
                        break
                    else:
                        break
                else:
                    ans = input("No such capital in the list. Want to add a new name to the dict? (y/n)").lower()
                    if ans == "y":
                        country = input("What's the name of a country with your capital? -->")
                        capital_country[capital]=country
                        break
                    else:
                        break

        elif action == 2:
            while True:
                country = input("Country (in Estonian): ").capitalize()
                if country in countries:
                    print("Capital: ", country_capital[country])
                    ans= input("\nFound a mistake in a capital name? (y/n)").lower()
                    if ans=="y":
                        del country_capital[country]
                        capital=input("Please write the right name of a capital (in Estonian) --> ")
                        country_capital[country] = capital
                        break
                    else:
                        break
                    
                else:
                    ans = input("No such country in the list. Want to add a new name to the dict? (y/n)").lower()
                    if ans == "y":
                        capital = input("What's the name of a capital with your country? -->")
                        country_capital[country]=capital
                        break
                    else:
                        break

        elif action == 3:
            p=0
            print("You'll be give 10 countries/capitals and you must guess which capitals/countries they belong:\n")
            for i in range (1, 10, 1):
                c_or_c = randint(1,2)
                if c_or_c == 2:
                    country = choice(countries)
                    capital = country_capital[country]
                    print(country)
                    ans=input("your answer: ").capitalize()
                    if ans == capital:
                        print("correct!\n")
                        p+=1
                    else:
                        print("wrong...\n")

                elif c_or_c == 1:
                    capital = choice(capitals)
                    country = capital_country[capital]
                    print(capital)
                    ans=input("your answer: ").capitalize()
                    if ans == country:
                        print("correct!\n")
                        p+=1
                    else:
                        print("wrong...\n")
            score = p*100/10
            print("Your score: ",score," %")



    else:
        print("Invalid input!")























# for key, value in riik_pealinn.items():
#      print(key+"-"+"\n")


