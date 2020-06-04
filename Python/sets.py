## Function sets.py
# Objectives:
#   1. Sets and subsets manipulation
#
# Input: None
# Output: Program prints out some manipulation with sets and subsets
#
# How to run this code:
#       python sets.py

#print('Welcome! This script manipulates sets and subsets.')

conj1 = {1,3,4,4} #it ignores what isn't unique (4)
conj1.add(2) #it automatically sorts -- conj = {1,2,3,4}
conj2 = {3,5,7}

# conj1 OR conj2
conj_uniao = conj1.union(conj2)

# conj1 AND conj2
conj_interseccao = conj1.intersection(conj2)

# conj1 MINUS conj2
conj_diff = conj1.difference(conj2)

# conj1 OR conj2 MINUS conj1 AND conj2
conj_sym_diff = conj1.symmetric_difference(conj2)

print('União: {un}\n'
 'Intersecção: {int}\n'
  'Diferença entre 1 e 2: {diff}\n'
  'Diferença simetrica: {sym_diff}'.format(
      un = conj_uniao, 
      int = conj_interseccao, 
      diff = conj_diff,
      sym_diff = conj_sym_diff))

conj_subset = {1,3}
print('Subset está contido em conj1? {}'.format(conj_subset.issubset(conj1)))

print('Conj1 contém subset? {}'.format(conj1.issuperset(conj_subset)))

print('Subset está contido em conj2? {}'.format(conj_subset.issubset(conj2)))

print('Conj2 contém subset? {}'.format(conj2.issuperset(conj_subset)))

# To  make  a list unique, we can transform it into a set

lista = ['cachorro', 'gato', 'gato', 'lobo']

lista = set(lista)
lista = list(lista)
