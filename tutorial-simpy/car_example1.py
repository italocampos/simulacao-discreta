# First one simulation
import simpy

def carro(ambiente):
	while True:
		print('Estacionando em {}'.format(ambiente.now))
		duracao_estacionamento = 5
		yield ambiente.timeout(duracao_estacionamento)

		print('Dirigindo em {}'.format(ambiente.now))
		duracao_direcao = 2
		yield ambiente.timeout(duracao_direcao)

ambiente = simpy.Environment()
processo = carro(ambiente)
ambiente.process(processo)
ambiente.run(until = 15)