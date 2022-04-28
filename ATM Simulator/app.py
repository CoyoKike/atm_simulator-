from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


while True: 
    balance = 0 
    #Registration
    name = input("Enter Name to register: ")
    name_lenght = len(name)
    if name_lenght >= 10:
        print("Your user name is ", name)
        while True:
            pin = input("Enter PIN: ")
            if len(pin) == 4:
                print(name + " has been registered with a starting balance of $" + str(float(balance)))
                break
            else: 
                print("Your PIN should at least be 4 digits long")
                continue
    else:
        print("Your name should be at least 10 characters long, please try again")
        continue
        
    #Login loop
    while True:
        print("          === Automated Teller Machine ===          ")
        print("LOGIN")
        name_enter = input("Enter name: ")
        pin_enter = input("Enter PIN: ")
        if name_enter == name and pin_enter == pin:
            print("Login Successful!")
            break
        else:
            print("Invalid Credentials! Try again")

    #Main Menu

    while True:
        atm_menu(name)
        option = input("Choose an option: ")
        if option == "1":
            account.show_balance(balance)
        elif option == "2":
            balance = account.deposit(balance)
        elif option == "3":
            balance = account.withdraw(balance)
        elif option == "4":
            account.logout(name)
            break
        else:
            print("I didn't understand, please try again")
        
