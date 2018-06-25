# -*- coding: utf-8 -*-

from random import gauss, random
from math import exp

def simulacao():
	fila = [] # Fila com os tempos de ocupação de linha de cada cliente
	hora = 3600 # Hora expressa em segundos
	minuto = 60 # Minuto expresso em segundos
	congestionado = 0 # Tempo de ocupação total dos canais
	pico = 0 # Numero de pico de ocupação de canais
	max_canais = 4000 # Número máximo de canais disponíves
	atendidos = 0 # Número de clientes atendidos
	rejeitados = 0 # Número de clientes rejeitados
	ligacoes = 0 # Número de ligações em cada unidade de tempo
	tempo = 0 # Unidade de tempo atual
	taxa = 60/100 # 100 ligações por minuto (equivale dizer que a cada 6/10 minuto, ocorrerá uma ligação). Expresso em segundos
	media = 4 # Media do tempo que um cliente passa em ligação (expressa em minutos)
	desvio = 1 # Desvio padrão em relação à média
	while tempo < 16 * hora:
		# Se há linhas ocupadas
		if fila != []:
			fila.sort()
			# print('#DEBUG:\nClientes ativos', len(fila))
			# Se um canal foi liberado
			if fila[0] <= tempo:
				fila.remove(fila[0])
				ligacoes -= 1
		# Se houve uma solicitação
		if random() < taxa:
			# Se há canais livres
			if ligacoes <= max_canais:
				ligacoes += 1
				atendidos += 1
				fila.append(abs(gauss(media * minuto, desvio * minuto)) + tempo) # adiciona à fila o tempo que o cliente vai ficar usando o canal
			# Se todos os canais estão ocupados
			else:
				rejeitados += 1
				congestionado += taxa
		if ligacoes > pico:
			pico = ligacoes
		tempo += taxa

	print('# RESULTADOS')
	print('Tempo de ocupação total dos canais: {h}h{m}m, {percent}%'.format(
		h = int(congestionado / hora),
		m = int(round((congestionado / hora - int(congestionado / hora)) * minuto, 0)),
		percent = round(congestionado / tempo * 100, 2)
		)
	)
	print('Número de clientes atendidos: {clientes}, {percent}%'.format(
		clientes = atendidos,
		percent = round(atendidos / (atendidos + rejeitados) * 100, 2)
		)
	)
	print('Número de clientes não atendidos: {clientes}, {percent}%'.format(
		clientes = rejeitados,
		percent = round(rejeitados / (atendidos + rejeitados) * 100, 2)
		)
	)
	print('Pico de ocupação de canais: {canais}, {percent}%'.format(
		canais = pico,
		percent = round(pico / max_canais * 100, 2)
		)
	)
