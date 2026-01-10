# 1. WAP TO PRINT THE SQUARE OF A NUMBER IF IT IS EVEN

a = int(input('Enter a number: '))

if a%2==0:
    print(f'The square of number is {a*2}')

# ___________________________________________________________________________________________#

# 2. WAP TO CHECK WHETHER A CHARACTER IS VOWEL OR NOT

a = input('Enter a character: ')

if a in 'AEIOUaeiou':
    print(f'Character {a} is a vowel.')

# _____________________________________________________________________________________________#

# 3. WAP TO PRINT ASCII VALUE OF THE CHARACTER ONLY IF IT IS UPPERCASE

n = input('Enter a value: ')

if 'A'<=n<='Z':
    print(f'ASCII value of the character {n} is {ord(n)}')

# _____________________________________________________________________________________________#

# 4. WAP TO PRINT CUBE OF A NUMBER ONLY IF IT IS DIVISIBLE BY 9 OR 6

a = int(input('Enter a value: '))

if a%9==0 or a%6==0:
    print(f'Cube of {a} is {a**3}')

# ______________________________________________________________________________________________#

# 5. WAP TO CHECK WHETHER A GIVEN INTEGER IS 3 DIGIT NUMBER.

a = int(input('Enter a value: '))

if 100<=a<=999:
    print(f'Number {a} is three digit number.')

# _____________________________________________________________________________________________#

# 6. WAP TO CHECK WHETHER A LAST DIGIT OF THE NUMBER IS 5

a = int(input('Enter a value: '))

if a%10==5:
    print(f'In this {a} value last digit is 5.')

# _______________________________________________________________________________________________#

# 7. WAP THO CHECK WHETHER THE GIVEN DATA IS FOLAT 

a = eval(input("Enter data: "))

if type(a) == float:
    print(f'Value {a} is float.')

# _______________________________________________________________________________________________#

# 8. WAP TO CHECK WHETHER THE GIVEN DATA IS SINGLE VALUE DATA.

a = eval(input('Enter data: '))

if type(a) in [int,float,complex]:
    print(f'{a} is {type(a)} and it is single value data.')

# _______________________________________________________________________________________________#

# 9. WAP TO CHECK WHETHER A GIVEN CHARACTER IS DIGIT OR NOT

a = input('Enter a value: ')

if a.isdigit():
    print(f'{a} is digit.')

# ___________________________________________________________________________________________________#

# 10. WAP TO CHECK WHETHER A GIVEN INTEGER IS MULTIPLE OF 3

a = int(input('Enter a value: '))

if a%3==0:
    print(f'{a} is multiple of 3.')
