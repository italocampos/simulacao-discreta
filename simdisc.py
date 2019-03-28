X = [0,3,1,6,3,4,1,3]

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