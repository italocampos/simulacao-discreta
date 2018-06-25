# -*- coding: utf-8 -*-
from random import random
from math import sqrt, exp

def randpoisson(exponencial):
	k = 0; p = 1
	while (p > exponencial):
		k += 1
		p = p * random()
	return k-1

def poisson(min, max, l, experiencias):
	exponencial = exp(-l)
	cont = 0
	for i in range(0, experiencias):
		k = randpoisson(exponencial)
		if min <= k <= max:
			cont += 1
	return cont/experiencias

# Função Probablilidade Densidade
def fdp(experiencias):
	cont = 0
	for i in range(0, experiencias):
		x = 2 * sqrt(random())
		if x < 0.5:
			cont += 1
	return cont/experiencias

def main():
	experiencias = 1000000
	#k1 = 4; k2 = 6; l = 5;
	print('Poisson: ', poisson(4, 6, 5, experiencias))
	print('Função Densidade Probablilidade: ', fdp(experiencias))

main()