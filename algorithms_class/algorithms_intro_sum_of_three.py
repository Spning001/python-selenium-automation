
# Our code generates a random three-digit number and has to sum up all its digits.
# For example, if a number is 349, the code has to print the number 16 because 3 + 4+ 9 = 16.

# code here
from random import randint

random_number = randint(100, 999)
print(f'The random number is: {random_number}')

result = 0

# solution A
# 0(n) linear time run time because it's a loop calculation
# for digit in str(random_number):
#     result = result + int(digit)
#
# print(f'Result: {result}')

# solution B
# random_number 321;  expected result = 6
# 0(n) linear time run time
while random_number != 0:
    result = result + (random_number % 10)
    random_number = random_number // 10


print(f'Result: {result}')
