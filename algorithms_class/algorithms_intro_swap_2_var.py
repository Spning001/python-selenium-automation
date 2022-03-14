# SWAP TWO VARIABLES

# User inputs two numbers.  One number is assigned to a variable, the other number is assigned to another variable.
# The task is to invert the variables, so that the first variable contains the second number,
# while the first number is in the second variable.

# code here
a = int(input('User input value for a: ')) #5
b = int(input('User input value for b: ')) #10

print(f'a = {a}, b = {b}')

# opt 1 - built-in function and without extra space
# a, b = b, a  #5, 10 = 10, 5

# opt 2 - using temp variable/extra space
# temp = a  #5
# a = b  #10
# b = temp  #5

# opt 3 - no built-in function and without extra space
# a = 5, b = 10
a = a + b  #a = 5 + 10 = 15
b = a - b  #b = 15 - 10 = 5
a = a - b  #a = 15 - 5 = 10

print(f'a = {a}, b = {b}')