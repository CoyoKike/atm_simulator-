

def show_balance(balance):
    print("Your balance is: " + str(float(balance)))

def deposit(balance):
    deposit = str(float(input("Enter amount to deposit: ")))
    current_balance = float(balance) + float(deposit)
    print("Current balance: ", current_balance) 
    return current_balance

def withdraw(balance):
    withdraw = float(input("Enter amount to withdraw: "))
    if float(withdraw) <= float(balance):
        current_balance = float(balance) - float(withdraw)
        print("Current balance: ", current_balance)
        return current_balance 
        
    else:
        print("Where are you going to get that kind of money?")
            


def logout(name):
    print("Goodbye ", name, "!")
 
 
