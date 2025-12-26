
"""
prices = [20,30,10]
total = 0
for price in prices:
    total += price
print(f"total price is: {total}")

"""
"""
numbers = [5,2,5,2,5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output +='x'
    print(output)
"""
# the multiplier 
"""
numbers = [2,5,8,10]
result = []
for number in numbers:
    result.append(number*2)
print(result)
"""
# the vowel counter 
"""
word = 'Looping through a string'
vowels = 'aeiouAEIOU'
count = 0
for letter in word:
    if letter in vowels:
        count +=1
print(f'The number of vowels in the word {word} is: {count}')
"""
# the pattern printer
"""
rows = 5
for row in range(rows+1):
    pattern =''
    for colum in range(row):
        pattern +='*'
    print(pattern)
"""
# the fizzbuzz
"""
result = 0
for number in range(1,51):
    if number % 3 == 0 or number %5 ==0:
        result += number
print(f'The sum of all numbers divisible by 3 or 5 between 1 and 50 is: {result}')

"""
# the reverse string
names = ['john', 'sarah', 'kelly','jams','bob','jenifer','zara']
# for name in reversed(names):
for name in names[::-1]:
   if name[0]=="j" or name[0]=="J":
       print(name)
       break
