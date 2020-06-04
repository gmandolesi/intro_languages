## Function contador_letras.py
# Objectives:
#   1. Count letters
#
# Input: None
# Output: None
#
# How to run this code:
#       python contador_letras.py

def conta_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade =  len(x)
        contador.append(quantidade)
    return contador

if __name__ == "__main__":
    lista=  ['cachorro', 'gato']
    print(conta_letras(lista))