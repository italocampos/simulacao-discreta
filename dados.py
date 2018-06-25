# -*- encoding: utf8 -*-
from random import randint

def dados(n_ensaios):
  sucesso = 0
  for i in range(1, n_ensaios+1):
    soma = 0
    for j in range(1, 3+1):
      soma += launchdice()
    if (10 <= soma <= 15):
      sucesso += 1
  return sucesso/n_ensaios

def launchdice():
  return randint(1, 6)

# main program
n_ensaios = 1000000
print('Numero de ensaios: ', n_ensaios)
print('Chance de se ter 10 <= soma <= 15: ', dados(n_ensaios))