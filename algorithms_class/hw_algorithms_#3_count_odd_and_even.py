
# Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

def count_odds_and_evens(x):
    odds = 0
    evens = 0

    while x != 0:
        curr_digit = x % 10
        if curr_digit % 2:
            odds += 1
        else:
            evens += 1
        x = x // 10

    return "evens: " + str(evens) + " odds: " + str(odds)

test_number = 34560 #expected evens = 3 and odds = 2
print(count_odds_and_evens(test_number))
