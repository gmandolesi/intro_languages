## Function lambdas.py
# Objectives:
#   1. Anonymous functions
#
# Input: None
# Output: None
#
# How to run this code:
#       python lambdas.py

# If a function can be described in one line, it is useful to describe it as anonymous

# nome da função   = lambda    variavel de entrada:    funcao
contador_letras2 = lambda lista: [len(x) for x in lista]
soma = lambda a,b: a + b

print(contador_letras2(['gato', 'lobo', 'cao']))
print(soma(5,14))

# dicionario de funcoes lambdas

calculadora = {
    'soma': lambda a,b: a+b,
    'subtracao': lambda a,b: a-b,
    'multiplicacao': lambda a,b: a*b,
    'divisao': lambda a,b: a/b,
}

print(type(calculadora))
soma_dict = calculadora['soma']
print(soma_dict(3,4))