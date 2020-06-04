## Function sets.py
# Objectives:
#   1. Module Import
#
# Input: None
# Output: None
#
# How to run this code:
#       python import_modules.py


# imports specific class
from methods_functions_classes import Calc

calculadora = Calc(10,5)
print(calculadora.soma())

# imports all classes within a file
import contador_letras

print(contador_letras.conta_letras(['bla', 'blee']))
