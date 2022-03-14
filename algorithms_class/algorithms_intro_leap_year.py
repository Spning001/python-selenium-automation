
# When a user enters a year, the code detects if i is a leap year.

# Leap years have the following characteristics
# Leap year is exactly divisible by 4 except for year ending in 00(cnetury year).
# The century year is a leap year only if it is perfectly divisible by 400.
#
# 2017 is not a leap year - 2017/4 = 504 r 1 (no)
# 1900 is not a leap year - 1900/400 = 4 r 300 (no)
# 2012 is a leap year - 2012/4 = 503 (yes)
# 2000 is a leap year - 2000/400 = 5 (yes)

# code here
year = int(input('Enter a year: '))

#0(1) constant time run time since there are no loop
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')