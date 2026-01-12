# ---------------------------------------------------------------------------- #
#   1. WAP TO CHECK WHETHER CHAR IS UPPER,LOWER,SPECIAL CHARACTER OR DIGIT     #
# ---------------------------------------------------------------------------- #
a = input("Enter input: ")

if 'A'<=a<="Z":
    print('Upper Case Character.')
elif 'a'<=a<='z':
    print('Lower Case Character')
elif '0'<=a<='9':
    print("Digit")
else:
    print('special character')

# 2. WAP TO CHECK WHETHER DIGIT IS ONE,TWO,THREE, OR GREATER THAN THREE DIGITS

a = int(input('Enter a value: '))
if 0<=a<=9:
    print('Single Digit')
elif 10<=a<=99:
    print('Double Digit')
elif 100<=a<=999:
    print('Triple Digit.')
else:
    print('Greater tha three digits.')

# ---------------------------------------------------------------------------- #
#           3.WAP TO CHECK GIVEN NUMBER IS LYING IN WHICH QUADRANT             #
# ---------------------------------------------------------------------------- #

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a>0 and b>0:
    print('Quadrant1')
elif a<0 and b>0:
    print('Quadrant2')
elif a<0 and b<0:
    print('Quadrant3')
elif a>0 and b<0:
    print('Quadrant4')

# ---------------------------------------------------------------------------- #
#                    4. WAP TO FIND GREATEST OF 3 NUMBERS                      #
# ---------------------------------------------------------------------------- #

a = int(input('Enter a value of a: '))
b = int(input('Enter a value of b: '))
c = int(input('Enter a value of c: '))

if a>b and a>c:
    print(f'a:{a} is greatest')
elif b>a and b>c:
    print(f'b:{b} is greatest')
else:
    print(f'c:{c} is greatest')

# ---------------------------------------------------------------------------- #
#                     5. WAP TO FIND SMALLEST OF 3 NUMBERS                     #
# ---------------------------------------------------------------------------- #

a = int(input('Enter a value of a: '))
b = int(input('Enter a value of b: '))
c = int(input('Enter a value of c: '))

if a<b and a<c:
    print(f'a:{a} is smalltest')
elif b<a and b<c:
    print(f'b:{b} is smalltest')
else:
    print(f'c:{c} is smalltest')

'''6. CONSIDER A CHARACTER IN UPPERCASE CONVERT IT INTO LOWERCASE AND
IF IT IS IN UPPERCASE CONVERT IT INTO LOWERCASE IF IT IS DIGIT PRINT IT'S
REMINDER IF IT IS DIVISIBLE BY 3 AND IF IT IS SPECIAL CHARACTER PRINT IT'S
ASCII VALUE. ''' 

a = input('Enter a data: ')

if 'A'<=a<='Z':
    print(a.lower())
elif 'a'<=a<='z':
    print(a.upper())
elif '0'<=a<='9' and int(a)%3==0:
    print(a)
else:
    print(ord(a))

'''7. WAP TO PRINT 'FIZZ' IF NUMBER IS MULTIPLE OF 3 PRINT 'BUZZ' IF
NUMBER IS MULTIPLE OF 5 AND PRINT'FIZZBUUZZ' IF NUMBER IS MULTIPLE OF 
3 AND 5 BOTH'''

a = int(input('Enter a number: '))

if a%3==0 and a%5==0:
    print('FizzBuzz')
elif a%3==0 :
    print('Fizz')
elif a%5==0 :
    print('Buzz')