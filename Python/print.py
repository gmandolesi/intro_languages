## Function print.py
# Objectives:
#   1. Data type manipulation
#   2. Arithmetic operations
#   3. Print function manipulation
#
# Input: User must input two values, as indicated in the prompt console
# Output: Program prints out:
#   1. The sum of the two values
#   2. Their subtraction
#   3. Their multiplication
#   4. Their division and rest
#   5. Their sum plus one
#   6. Their division ignoring decimal places
#
# How to run this code:
#       python print.py

print('Welcome! This script will perform basic arithmetic functions between two values of your choice.')

a = int(input('Please enter the first value: '))
b = int(input('Please enter the second value: '))

# Arithmetic operations
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
x = '1'

# Number printing
print (soma)

# String + number concatenation
print ('subtracao: ' + str(subtracao))

# Indirect printing
print ('multiplicacao: {}'.format(multiplicacao))

print ('divisao: {}\nresto: {}'. format(divisao, resto))

# Manipulation so that order doesn't matter
print ('soma + 1: {sum}\n'
        'divisao (int): {div}'.format(
            div = int(divisao),
            sum=soma + int(x)))
