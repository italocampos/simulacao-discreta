from Aleatorio import *
import math

volume_tanque = 2000
media_litros = 15
desvio_litros = 2
media_despejo = 4
max_despejo = 10
nexp = 1000
total = 0

ale = Aleatorio()

for i in range(nexp):
	dias = 0
	volume_atual = 0
	while (volume_atual < volume_tanque):
		expmedia = math.exp(-media_despejo)
		qtde_despejos = ale.randpoi(expmedia) - 1
		
		if (qtde_despejos > 10):
			qtde_despejos = 10

		for i in range(qtde_despejos):
			
			expmedia = math.exp(-media_litros)
			qtde_agua = ale.randpoi(expmedia)
			
			if (qtde_agua + volume_atual <= volume_tanque):
				volume_atual += qtde_agua
			else:
				volume_atual = volume_tanque
		
		dias += 1
	total += dias

print(total/nexp)