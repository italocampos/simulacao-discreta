# -*- encoding: utf8 -*-
from random import randint


def jacare(n_ovos, n_ensaios):
  pmacho = 0.6
  pfemea = 1 - pmacho
  sucesso = 0
  for i in range(1, n_ensaios+1):
    macho = 0
    femea = 0
    for j in range(1, n_ovos+1):
      ovo = randint(1, 100)
      if ovo <= pmacho*100:
        macho += 1
      else:
        femea += 1
    if (4 <= macho <= 6):
      sucesso += 1
  return sucesso/n_ensaios
  
# main program
n_ovos = 10
n_ensaios = 1000000
print('Numero de ovos: ', n_ovos)
print('Numero de ensaios: ', n_ensaios)
print('Chance de se ter 4 <= machos <= 6: ', jacare(n_ovos, n_ensaios))