from random import gauss
from random import randint
from random import random
from math import sqrt
from math import exp
# Arquivo de prova

EXP = 1000000

def questao_2(ensaios):
	lucro = 0
	for _ in range(0, EXP):
		for _ in range(0,ensaios):
			# Comprimento em mm
			haste = gauss(200, 2)
			if haste < 198:
				lucro += 150
			else:
				lucro += 200
	return lucro/EXP

def play_dice():
	return randint(1,6)

def questao_3():
	counter = 0
	for _ in range(0, EXP):
		if play_dice() + play_dice() in [7, 8]:
			counter += 1
	return counter/EXP

def questao_5():
	counter = 0
	for _ in range(0, EXP):
		x = sqrt(3*random() + 1)
		y = exp(x)
		if y < 3.5:
			counter += 1
	return counter/EXP