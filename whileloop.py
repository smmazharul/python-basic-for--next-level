"""
i = 1
while i<=5:
    print("*" * i)
    i +=1

"""
# Gussing number game
"""
secret_number = 8
guessing_count = 0
guessing_limit = 3

while guessing_count<guessing_limit:
    guess = int(input("Guess: "))
    guessing_count +=1
    if guess == secret_number:
        print("You Won!")
        break
else:
    print("You Loss!")

"""

# car game using while loop

command  = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car start...")
    elif command == "stop":
        if not started:
            print("car is already stoped")
        else:
            started = False
            print("Car stop.." )
    elif command == "help":
        print("""
start = car will start 
stop = car will stop 
quit = to quit


        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")
        