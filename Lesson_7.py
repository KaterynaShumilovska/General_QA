#Task 1
def simple_calc(a, b, o):
    if o in ('+', '-', '*', '/'):
        if o == '+':
            return a+b
        elif o == '-':
            return a-b
        elif o == '*':
            return a*b
        else:
            return a/b
    else:
        return (f'Not known operation: {o}')

a = float(input('Enter number1:'))
b = float(input('Enter number2:'))
o = str(input('Enter operation:'))

print(simple_calc(a, b, o))

#Task 2
from math import sqrt
def prop_square(l):
    return tuple({f'Perimeter: {4*l}',f'Area: {l**2}', f'Diagonal: {l*sqrt(2)}'})

l = float(input('Enter the side length of a square to calculate its perimeter, area and diagonal: '))

print(prop_square(l))

#Task 3
def is_prime(r):
    if (r >= 2) and (r <= 1000):
        for i in range (2, r//2+1):
            if r%i == 0:
                return False
        return True
    else:
        return 'Wrong number!'

r = int(input('Enter a number from 2 to 1000: '))

print(is_prime(r))

