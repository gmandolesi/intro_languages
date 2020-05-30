## Function print.py
# Objectives:
#   1. Conditional programming (if, elif)
#   2. Logical operations (and, or, not)
#
# Input: User must input two values, as indicated in the prompt console
# Output: Program prints out:
#   1. The greatest value
#   2. Whether the numbers are even or odd
#   3. Whether both of them are positive
#   4. Whether any is negative
#   5. Whether any is zero
#
# How to run this code:
#       python conditional.py

print('Welcome! This script performs basic comparison between two values of your choice.')

a = int(input('Please enter the first value: '))
b = int(input('Please enter the second value: '))

# Which value is greater?
if a>b:
    print('The first value, {}, is greater.'.format(a))
elif (a<b):
    print('The second value, {}, is greater.'.format(b))
else:
    print('The values are the same.')

# Are they even or odd?
resto_a = a % 2
resto_b = b % 2

if resto_a:
    print('{} is odd.'.format(a))
else:
    print('{} is even.'.format(a))

if not resto_b:
    print('{} is even.'.format(b))
else:
    print('{} is odd.'.format(b))

if a>0 and b>0:
    print('Both values are positive.')

if a<0 or b<0:
    print('At least one value is negative.')

if not (a and b):
    print('At least one value is zero.')