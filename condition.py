"""
is_hot = False
is_cold = False
if is_hot:
    print("Today is hot day")
    print("Drink plenty of water")

elif is_cold:
    print("Today is cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print('Enjoy your day')

"""

"""
price = 1000000
has_good_creadit = False
if has_good_creadit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"Down Payment is: ${down_payment}")

"""

# problem one
""" num = -1

if num > 0:
    print(f"{num} is positive")
elif num<0:
    print(f"{num} is nagetive")
else:
    print(f"{num} is zero") 
"""
#problem two
"""
score = int(input("Enter your score 0 to 100: "))
if score<0 or score>100:
    print("Enter valid score number 0 to 100")
elif score>=80:
    print("you grade point is A")
elif score >=60 and score<80:
    print("your grade point is: B")
elif score >=40 and score<60:
    print("your grade point is: C")

else:
    print("your grade point is: Fail")
"""

hour = int(input("Enter the time: 0 to 23 "))

if hour <0 or hour>23:
    print("Enter valid time 0 to 23")
elif hour>= 5 and hour<12:
    print("Morning")
elif hour<= 12 and hour <17:
    print("Afternoon")
elif hour<=17 and hour<21:
    print("Evining")
else:
    print("Night")