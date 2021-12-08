print("---Welcome to Teerapoom Coffee---")
show = int(input("Please type 1 to show menu: "))
hot = 55
cold = 60
if show == 1:
    print("---choose to the menu---")
    print("1. Espresso")
    print("2. Cappucino")
    print("3. Latte")
    print(" ")
    Coffe_Menu = int(input("Select coffee: "))
    if Coffe_Menu > 0 and Coffe_Menu <= 3:
        print("---Choose the type of coffee---")
        print("1. Hot 55 baht")
        print("2. Cold 60 baht")
        print(" ")
        Menu_choice = int(input("Select type: "))
        if Menu_choice == 1:
            print("---You chose hot Latte 55 baht---")
            print(" ")
            money_hot = int(input("Input your money: "))
            if money_hot >= 55:
                print("You recieved a change %d baht" % (money_hot - hot))
                print("---Thank you---")
            else:
                print("Not enough money")
                print("---Please try again---")
        elif Menu_choice == 2:
            print("---You chose cole Latte 60 baht---")
            print(" ")
            money_cold = int(input("Input your money: "))
            if money_cold >= 60:
                print("You recieved a change %d baht" % (money_cold - cold))
                print("---Thank you---")
            else:
                print("Not enough money")
                print("---Please try again---")
        else:
            print("Please select a new one")
    else:
        print("No new menu")
else:
    print("Sorry , something went wrong")
