## Function loops.py
# Objectives:
#   1. Loops (for, while, range)
#
# Input: User must input the maximum value, as indicated in the prompt console
# Output: Program prints out all the prime numbers until the user indicated maximum value
#
# How to run this code:
#       python loops.py

print('Welcome! This script informs all the prime numbers until a value of your choice.')

user_input = int(input('Please enter a value smaller than 100: '))

while user_input >= 100:
    user_input = int(input('The value you have entered is equal or greater than 100. Please insert a valid value: '))

for num in range (user_input):
    div = 0
    for aux in range (1, num+1):
        resto = num % aux
        if resto == 0:
            div += 1
            if div > 2:
                continue

    if div == 2:
        print (aux)
