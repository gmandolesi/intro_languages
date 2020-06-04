## Function files.py
# Objectives:
#   1. Files manipulation
#
# Input: None
# Output: None
#
# How to run this code:
#       python files.py

# open file in overwrite mode. if it doesn't exist, it is created.
def escrever_arquivo(filename, texto):
    arquivo = open(filename, 'w')
    arquivo.write(texto)
    arquivo.close()


# open file in append mode. if it doesn't exist, it is created.
def atualizar_arquivo(filename, texto):
    arquivo = open(filename, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(filename):
    arquivo = open(filename, 'r')
    return arquivo.read()

def inserir_notas_exemplo(filename):
    atualizar_arquivo(filename, 'Rafa,10,10,5\n')
    atualizar_arquivo(filename, 'Ju,4,6,5\n')
    atualizar_arquivo(filename, 'Gui,2,3,5\n')

def calcular_media(filename):
    # list comprehension
    media = lambda notas: int(sum([int(i) for i in notas])/3)

    notas = ler_arquivo(filename)
    notas = notas.split('\n')
    lista_media = []
    for x in notas:
        lista_notas = x.split(',')
        aluno = lista_notas.pop(0)

        print(aluno)
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copiar_arquivo(filename):
    #same as cp in bash. can copy or rename
    import shutil
    shutil.copy(filename, '..')

def mover_arquivo(filename):
    # same as mv in bash. can move or rename
    import shutil
    shutil.move(filename, '..')

if __name__ == "__main__":
    escrever_arquivo('teste.txt', 'Hello World!\n')
    atualizar_arquivo('teste.txt', 'Welcome!\n')
    ler_arquivo('teste.txt')

    #inserir_notas_exemplo('notas')

    print(calcular_media('notas'))