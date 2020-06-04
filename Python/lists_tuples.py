## Function lists_tuples.py
# Objectives:
#   1. List manipulation
#   2. Tuple manipulation
#
# Input: None
# Output: Program prints out some manipulation with lists and tuples.
#
# How to run this code:
#       python lists_tuples.py

#print('Welcome! This script manipulates lists and tuples.')

lista = [1,10,7,5,2]
lista_animal = ['cachorro', 'gato', 'elefante']

print(lista_animal[1])
for x in lista_animal:
    print(x)

print(sum(lista))
print(max(lista))

print(max(lista_animal)) #última palavra na ordem alfabética

#ordena de menor pra maior ou por ordem alfabética
lista.sort()
lista_animal.sort()

#inverte a ordem do vetor
lista.reverse()
lista_animal.reverse()

if 'gato' in lista_animal:
    print('existe gato na lista')
else:
    print('não existe gato na lista')
    lista_animal.append('gato')
    print('gato foi adicionado à lista')

#para repetir as entradas
lista_triplicada = lista_animal * 3
lista_num_triplicada = lista * 3

lista_triplicada.pop() #remove o último item da lista
lista_triplicada.pop(0) #remove o primeiro item da lista
lista_animal.remove('gato') #remove o gato da lista

#tuplas (imutáveis)
tupla = (1,10,12,14)
tupla_animal = tuple(lista_animal)
lista_tupla = list(tupla)

#tamanho
print(len(lista))
print(len(lista_animal))
print(len(tupla_animal))
print(len(tupla))