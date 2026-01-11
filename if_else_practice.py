# ---------------------------------------------------------------------------- #
#              1. WAP TO CHECK WHETHER THE DATA IS MUTUABLE OR NOT             #
# ---------------------------------------------------------------------------- #

a = eval(input('Enter a data: '))

if type(a) in [list,set,dict]:
    print(f'{a} is {type(a)} and it is mutuable data type.')
else:
    print(f'{a} is {type(a)} and it is immutable data type.')

# ---------------------------------------------------------------------------- #
#            2. WAP TO CHECK WHETHER A GIVEN CHARACTER IS DIGIT OR NOT            #
# ---------------------------------------------------------------------------- #

a = input('Enter data: ')

if a.isdigit():
    print(f'{a} is digit.')

else:
    print(f'{a} is not digit.')

# ---------------------------------------------------------------------------- #
#            3. WAP TO CHECK WHETHER A GIVEN CHARACTE IS SPECIAL OR NOT           #
# ---------------------------------------------------------------------------- #

n = input('Enter a data: ')

if 'A'<=n<='Z' or 'a'<=n<='z' or '0'<=n<='9':
    print(f'{n} is not a special character.')
else:
    print(f'{n} is special character.') 

# ---------------------------------------------------------------------------- #
#         4. WAP TO CHECK WHETHER A LIST CONSIST OF MIDDLE VALUE OR NOT        #
# ---------------------------------------------------------------------------- #

a = eval(input('Enter list: '))

if len(a)%2!=0:
    character = len(a)//2
    print('There is a middle character',a[character])
else:
    print('There is no middle character.')

# ---------------------------------------------------------------------------- #
#                5. WAP TO CHECK WHETHER A NUMBER IS EVEN OR ODD               #
# ---------------------------------------------------------------------------- #

a = int(input('Enter a number: '))

if a%2==0:
    print(f'{a} is even number.')
else:
    print(f'{a} is odd number.')

# ---------------------------------------------------------------------------- #
#            6. WAP TO CHECK WHETHER A DATA IS MUTUABLE OR IMMUTABLE           #
# ---------------------------------------------------------------------------- #

a = eval(input('Enter a data: '))

if type(a) in [list,set,dict]:
    print(f'{a} is mutuable.')
else:
    print(f'{a} is immutuable.')

# ---------------------------------------------------------------------------- #
#      7. WAP TO CHECK WHETHER 2 VALUES POINTING TO THE SAME MEMORY OR NOT     #
# ---------------------------------------------------------------------------- #

a = input('Enter a value of a: ')
b = input('Enter a value of b: ')

if a is b:
    print(id(a))
    print(id(b))
    print(f'{a} and {b} are sharing same memory.')
else:
    print(f'{a} and {b} are not sharing same memory.')

# ---------------------------------------------------------------------------- #
#    8.CONSIDER TUPLE OF LENGTH 2 AND CHECK WHETHER IT IS HOMOGENOUS OR NOT    #
# ---------------------------------------------------------------------------- #

a = eval(input("Enter a tuple of 2 value: "))

if type(a[0]) == type(a[1]):
    print('Tuple is homegenous')
else:
    print('Tuple is not homogenous')

# ---------------------------------------------------------------------------- #
#             9. WAP TO CHECK WHETHER A STRING IS PALINDROME OR NOT            #
# ---------------------------------------------------------------------------- #

a = input('Enter a string: ')

if a == a[::-1]:
    print('String is palindrome')
else:
    print('String is not palindrome')

# ---------------------------------------------------------------------------- #
#           10. WAP TO CHECK WHETHER A NUMBER IS POSITIVE OR NEGATIVE          #
# ---------------------------------------------------------------------------- #

a = int(input('Enter a number: '))

if a >=0:
    print(f'{a} is positive number.')
else:
    print(f'{a} is negative number.')


