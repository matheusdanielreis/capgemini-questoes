password = input()

min = 6 #minimum of characters
number = len(password) #password character numbers

if number < min:
    print(f'{(min - number)}')
