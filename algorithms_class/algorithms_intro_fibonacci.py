
# The Fibonacci sequence is a type series where each number is the sum of the two that precede it.
# It starts from 0 and 1 usually.
#
# The equation for the Fibonacci sequence:
# φ0 = 0, φ1 = 1, φn=φn-1 + φn-2
#
# Fibonacci Sequence formula
# Fn = Fn-1 + Fn-2
# if n = 3, then calculation is as follows
# F0 = 0
# F1 = 1
# F2 = F1 + F0 = 0 + 1 = 1
# F3 = F2 + F1 = 1 + 1 = 2

# 1, 1, 2
# the Fibonacci number is 2

# 0(n) linear time run time because it's a loop calculation
def fibonacci(n):
    if n < 0:
        return 'Not a valid value'
    if n == 0:
        return 0
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    result = [1, 1]
    index = 3

    while index <= n:
        result.append(result[-1] + result[-2])
        index = index + 1

    return result

print(fibonacci(5))
print(fibonacci(3))