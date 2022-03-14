
# When user enters a number, its factorial is displayed.

# code here

import math

number = int(input('User input a number: '))  # number = 5

# using math function
#print(math.factorial(number))  #factorial of 5 is 120
    # 1 * 2 * 3 * 4 * 5 = 120

# not using math function
# 0(n) linear time run time because it's a loop calculation
result = 1
if number != 0:  #if number(user input) does not = 0, go to next line, but if number = 0, result is 1 which is given.
    for i in range(1, number + 1):  #for i(variable) in range(1, number + 1):
        result = result * i  #result *= i
        # result = 1 * 1
        # result = 1 * 2
        # result = 2 * 3
        # result = 6 * 4
        # result = 24 * 5
        # result = 120

print(f'Result = {result}')