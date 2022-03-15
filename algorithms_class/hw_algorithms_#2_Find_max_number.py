
# Find max number from 3 values, entered manually from a keyboard.

user_numb1 = int(input('Please input 1st value: '))
user_numb2 = int(input('Please input 2nd value: '))
user_numb3 = int(input('Please input 3rd value: '))

def max(user_numb1, user_numb2, user_numb3):
    if (user_numb1 > user_numb2) and (user_numb1 > user_numb3):
        max_numb = user_numb1
    elif (user_numb2 > user_numb1) and (user_numb2 > user_numb3):
        max_numb = user_numb2
    else:
        max_numb = user_numb3
    print('The largest number is = ', max_numb)

max(user_numb1, user_numb2, user_numb3)