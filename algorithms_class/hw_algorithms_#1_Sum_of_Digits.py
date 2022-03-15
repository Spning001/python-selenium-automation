
# Compute the sum of digits in all numbers from 1 to n.  When a user enters a number n, find the sum of digits in all
# numbers from 1 to n.

user_input = int(input('User enters a number: '))

result = 0

if user_input != 0:
    for i in range(1, user_input + 1):
        result = result + i


print(f'Result = {result}'