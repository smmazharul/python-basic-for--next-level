
def result():
    print(f"the value is {value:.2f}")

def add(value):
   nums = float(input("Enter the value: "))
   return nums + value

def substrac(value):
    nums = float(input("Enter the value: "))
    return nums - value

def devided(value):
    nums = float(input("Enter the value: "))
    return nums / value

def multipy(value):
    nums = float(input("Enter the value: "))
    return nums * value

value = 0
is_runing= True

while is_runing:
    print("********************")
    print("     Calculatoe     ")
    print("********************")

    print("0 : result")
    print("1 : sum")
    print("2 : substrac")
    print("3 : devided")
    print("4 : multipy")
    print("5 : exit")

    option = input("Enter the option number: ")

    if option == '0':
        result()

    elif option == '1':
        value = add(value)
    
    elif option == '2':
        value = substrac(value)
    elif option == '3':
         value = devided(value)
    elif option == '4':
        value = multipy(value)

    elif option == '5':
        is_runing =False
    else:
        print("Invalid input")



print("********************")
print(f"The value is: {value:.2f}")
print("********************")
