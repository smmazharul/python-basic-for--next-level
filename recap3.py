# # function
# def add(a,b):
#     sum = a+b
#     return sum
# print(add(2,3))

# # function with default arguments with keyword arguments
# def greet (name="username",age=18):
#     print(f"Hello {name}, you are {age} years old.")
# greet(age=25)

# Function with multiple positional arguments
# def sum(*nums):
#     total =0
#     for num in nums:
#         total +=num
#     return total
# print("sum of: ",sum(1,2,3,4,5))

# # function with multiple keyword arguments
# def info(**data):
#     for key,value in data.items():
#         print(f"{key:10}: {value}")
    

# print(info(name="Alice", age=30, city="New York", profession="Engineer"))


# # Read input
# input_string = input("Enter two digits separated by space: ")
# digit_x, digit_y = map(int, input_string.split())


# # Check divisibility avoiding division by zero
# if digit_x != 0 and digit_y % digit_x == 0:
#     print("YES")
# elif digit_y != 0 and digit_x % digit_y == 0:
#     print("YES")
# else:
#     print("NO")

"""
Problem Statement
In the kingdom of Parityland, the king has issued a challenge to his advisors. He presents a row of stones, each marked with an integer. The stones are arranged in positions numbered from 1 to N. The king wants to know if it's possible to rearrange the stones so that for every position  () , the sum of the stone's number placed at position  and the position  itself is always even or always odd for all stones.

Formally, after rearranging the stones, for all i (), the value of  +  must have the same parity — either all even or all odd.

Your task is to help the king by determining whether such a rearrangement exists.

Input Format

The first line contains an integer  — the number of test cases.
The second line contains an integer  — the number of stones.
The third line contains  space-separated integers representing the numbers on the stones.
Summation of  over all test cases doesn't exceed .
Constraints

Output Format

Print "YES" if there exists any rearrangement that satisfies the king's condition. Otherwise, print "NO". Don't forget to print a newline after each test case.
"""
# def can_rearrange_stones(n, stones):
#     even_count = sum(1 for stone in stones if stone % 2 == 0)
#     odd_count = n - even_count

#     if even_count == 0 or odd_count == 0:
#         return "YES"
#     else:
#         return "NO"
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     stones = list(map(int, input().split()))
#     result = can_rearrange_stones(n, stones)
#     print(result)
            
# # Importing custom module


