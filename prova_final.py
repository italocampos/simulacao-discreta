# -*- coding: utf-8 -*-

from random import gauss

def questao_2():
	hora = 60
	nexp = 1000000
	desencontro = 0
	for _ in range(0, nexp):
		trem_a = gauss(mu = 7*hora, sigma = 10)
		trem_b = gauss(mu = 7*hora, sigma = 5)
		if abs(trem_a - trem_b) > 3:
			desencontro += 1
	return desencontro/nexp

def questao_3(var):
	hora = 60
	nexp = 100000
	desencontro = 0
	for _ in range(0, nexp):
		trem_a = gauss(mu = 7*hora, sigma = 10)
		trem_b = gauss(mu = 7*hora, sigma = 5)
		if abs(trem_a - trem_b) > var:
			desencontro += 1
	return desencontro/nexp

def teste():
	var = 15
	while questao_3(var) > 0.05:
		var += 1
	return var

def questao_4():
	nexp = 100000
	exp = 0
	sucesso = 0
	while exp < nexp:
		x = gauss(0, 1)
		if x > 1:
			if x**2 + x > 4:
				sucesso += 1
			exp += 1
	return sucesso/exp

def main():
	print("Questão 2:")
	print("A chance é de ", questao_2(), " de desencontro.")
	print("Questão 3:")
	print("O tempo deve ser de ", teste(), " minutos.")
	print("Questão 4:")
	print("A probalilidade é de ", questao_4())