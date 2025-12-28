questions = ("What is the capital of France? ",
             "What is 2 + 2? ",
             "What is the largest planet in our solar system? ",
             "Who wrote 'To Kill a Mockingbird'? ")

options = (("A. London", "B. Berlin", "C. Paris", "D. Madrid"),
           ("A. 3", "B. 4", "C. 5", "D. 6"),
           ("A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"),
           ("A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"))

answers = ("C", "B", "B", "A")
guess_answers = []
question_number = 0
score = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Enter your answer (A, B, C, or D): ").upper()
    guess_answers.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"The correct answer is {answers[question_number]}.")
    question_number += 1


print("--------------------------")
print("------Quiz Completed!-----")
print("--------------------------")

for answer in answers:
    print(answer, end=" ")

print()
for guess in guess_answers:
    print(guess, end=" ")
print()

score_percentage = int((score / len(questions)) * 100)
print (f"your score is {score_percentage}%")
