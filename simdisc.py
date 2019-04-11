import statistics as st
import math
from copy import copy

# conjuntos de dados
X = [0,3,1,6,3,4,1,3]
A = [58.6482, 60.7688, 57.9416, 58.8650, 60.5505, 61.5079, 58.4430, 59.1439, 59.7513, 61.7646, 59.1022, 59.2938, 61.8068, 59.9236, 60.1800, 58.6753, 60.9961, 59.1470, 61.2076, 61.0790, 61.0359, 60.7524, 59.0461, 61.1086, 59.8184, 61.2934, 61.4001, 61.2937, 57.3782, 61.2049, 59.7765, 60.8209, 61.2855, 60.8319, 59.7009, 60.2464, 60.4145, 60.6598, 58.7840, 60.1347, 59.0217, 60.4803, 61.0445, 59.5986, 60.3876, 58.8829, 60.0900, 58.7793, 59.5580, 59.3169, 58.7369, 59.1403, 58.7313, 59.2234, 59.4756, 58.3702, 59.6124, 57.7219, 60.3160, 59.2787, 59.5117, 59.6192, 60.1209, 59.5806, 58.7161, 60.3290, 59.2428, 60.6603, 59.2318, 59.8816, 60.7025, 59.7575, 60.6408, 58.7476, 59.0084, 61.8732, 60.0859, 60.2366, 59.0289, 59.2829, 60.0155, 59.1466, 58.4206, 60.2357, 59.9757, 60.2416, 60.0236, 58.1723, 59.7747, 60.5153, 59.7560, 60.7227, 58.9124, 60.7652, 57.3110, 60.6493, 60.1931, 59.9564, 61.2574, 61.2378, 60.7688, 59.1084, 60.7788, 59.7590]

def media(conjunto):
	soma = 0
	for elemento in conjunto:
		soma += elemento
	return soma/len(conjunto)

def mediana(conjunto):
	conjunto.sort()
	n = len(conjunto)
	meio = int(n/2)
	if n % 2 != 0:
		return conjunto[meio]
	else:
		return (conjunto[meio] + conjunto[meio-1])/2

def variancia(conjunto):
	soma = 0
	med = media(conjunto)
	for elemento in conjunto:
		soma += (elemento - med)**2
	return soma/len(conjunto)

def quartis(conjunto):
	dados = sorted(conjunto)
	meio = len(dados)//2
	q1 = mediana(dados[:meio])
	q2 = mediana(dados)
	q3 = mediana(dados[meio:])
	return q1, q2, q3

def amplitude(conjunto):
	return max(conjunto) - min(conjunto)

def desvio_padrao(conjunto):
	return math.sqrt(variancia(conjunto))

def coeficiente_variacao(conjunto):
	return desvio_padrao(conjunto) / media(conjunto) * 100

def coeficiente_assimetria(conjunto):
	_, _, q3 = quartis(conjunto)
	return q3/(mediana(conjunto)**(3/2))

def moda(conjunto):
	frequencias = []
	i = 0
	while i < len(conjunto):
		frequencias.append((conjunto[i], conjunto.count(conjunto[i])))
		conjunto = remove(conjunto[i], conjunto)
	maior = frequencias[0]
	for dic in frequencias[1:]:
		if dic[1] > maior[1]:
			maior = dic
	return maior[0]

def remove(elemento, conjunto):
	copia = copy(conjunto)
	for numero in conjunto:
		if numero == elemento:
			copia.remove(numero)
	return copia