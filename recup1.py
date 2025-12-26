#problem one 
"""
i = 1
while i <=10:
    if i % 2 ==0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")
    i+=1
"""
#problem 2
"""
while True:
    number = int(input("Enter a Number: "))
    if number>0:
        print(f"{number} is positive value" )
    elif number<0:
        print(f"{number} is Nagetive value")
    else:
        break
"""

# problem 3 
"""
secret_number = 7
while True:
    guess = int(input("Guess Number: "))
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("You Guessed it!")
        break
"""
#problem 4

given_number = int(input("Enter a number: "))

while given_number<=1:
    if i % 3==0:
        print(f"{i} is Divisible by 3")
    else:
        print('Number is: ', i)
    i+=1
