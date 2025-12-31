
def balance ():
    print(f"Your current balance is: {curr_balance:.2f}")


def deposit():
    dep_amount = float(input("Enter the amount for deposit: "))
    if dep_amount < 0:
        print("Enter the valid amount must be positive number")
        return 0
    else:
        return dep_amount 

def withdraw():
    withdraw_balance = float(input("Enter the amount for withdraw: "))
    if withdraw_balance <0:
        print("Enter the valid amount must be positive number")
        return 0
    elif withdraw_balance > curr_balance:
        print("Ensificant balanace ")
        return 0
    else:
        return withdraw_balance



curr_balance = 0
is_running = True
while is_running:
    print("1 : Balance check ")
    print("2 : Deposit ")
    print("3 : Withdraw ")
    print("4 : Exit ")

    choice = input("Enter the option number: ")

    if choice == '1':
        balance()
    elif choice == '2':
        curr_balance += deposit()
    elif choice == '3':
        curr_balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Not valid choice")
