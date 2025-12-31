
# def local_function():
#     x =10
#     print(x)
# local_function()
# print(x)  # This will raise an error because x is not defined in this scope

# x = "global variable"

# def access_global():
#     global x
#     x = "modified global variable"
#     print(x)

# access_global()
# print(x)  # This will print "modified global variable"

# x = 'global'

# def outer():
#     x="enclosing"
#     def inner():
#         x='inner'
#         print(x)
#     inner()
# if __name__ == "__main__":
#     outer()


def welcome_greeting():
    print("welcome to new things in python")
if __name__ == "__main__":
    welcome_greeting()

