# Function in python

# def greet(name,age):
#     print(f"Hello, my name is {name}")
#     print(f"I am {age} years old.")
#     print("For example:")
#     print()
# greet("Mazharul",27)
# greet("Humayra",25)
# greet("Fahim",14)

# def add(a,b):
#     sum = a +b
#     return sum

# def substract(a,b):
#     difference = a-b
#     return difference

# def multiply(a,b):
#     product = a*b
#     return product

# def divide(a,b):
#     quotient = a//b
#     return quotient

# print(add(5,3))
# print(substract(10,4))
# print(multiply(2,6))
# print(divide(8,2))
# import time
# name_list =[]

# def create_name(first,last):
#     full_name = f'{first.capitalize()} {last.capitalize()}'
#     return full_name


# is_running = True
# while is_running:
#     add_first_name = input("Enter first name (q to quit): ")
    
#     if add_first_name.lower()=='q':
#         print("Exiting the program.")
#         is_running = False
#     else:  
#         add_last_name = input("Enter last name (q to quit): ")
#         name = create_name(add_first_name,add_last_name)
#         name_list.append(name)

# for name in name_list:
#     time.sleep(1)
#     print(name)




# Function with keyword arguments
# def greeting(name,title,age):
#     print(f"{name} is a {title} and {age} years old.")

# greeting(age=27,title="Student",name="Mazharul")

# function with arbitary arguments
#  function with *args
def multiply(*nums):
    product = 1
    for num in nums:
        product *=num
    return product
print(multiply(2,3,4))

# function with **kwargs

def build_person(**info):
    for key,value in info.items():
        print(f"{key.upper():10} : {value}")

build_person(name="Mazharul",
            age=27,
            city="Dhaka",
            profession="Student", 
            hobby="Coding", 
            country="Bangladesh")