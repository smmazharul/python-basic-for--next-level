# list, tuple, set, dictionary and string
# membership operator: in, not in

word = "hello world"

input_word = input("Enter a letter to check: ")

if input_word not in word:
    print(f"'{input_word}' is found in '{word}'")
else:
    print(f"'{input_word}' is not found in '{word}'")