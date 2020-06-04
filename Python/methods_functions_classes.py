## Function sets.py
# Objectives:
#   1. Methods 
#   2. Functions (Methods with return)
#   3. Classes
#
# Input: None
# Output: Program prints out some manipulation with sets and subsets
#
# How to run this code:
#       python sets.py

#print('Welcome! This script introduces methods, functions and classes')

class Calc: #conventionally, classes have their first characters in capital letters
    def __init__(self, num1, num2): #this method is run every time you create a Calc object
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

class Calc2: #conventionally, classes have their first characters in capital letters
    def __init__(self): #optional
        pass

    def soma(self, a, b):
        return a + b

if __name__ == '__main__': # this will only be executed if the source file  is run. if it is imported, this code fragment is ignored

    calculadora = Calc(10,2)
    print(calculadora.soma())

    calculadora2 = Calc2()
    print(calculadora2.soma(10,2))