# Second one simulation:
# - Modeling the car as a class;
# - Yelding a process;
import simpy
from random import randint

class Carro(object):
	def __init__(self, ambiente):
		self.env = ambiente
		# Executa o método run toda vez que uma instância é criada
		self.action = ambiente.process(self.run())

	def run(self):
		while True:
			print('Estacionando e carregando em {}'.format(self.env.now))
			tempo_carga = randint(5,20)
			# Yield siginifica que o processo charge() será finalizado para
			# depois continuar a execução ddo método run()
			yield self.env.process(self.charge(tempo_carga))

			# O processo charge() terminou e o carro voltará a andar
			print('Dirigindo em {}'.format(ambiente.now))
			duracao_direcao = randint(10,50)
			yield self.env.timeout(duracao_direcao)

	def charge(self, duracao):
		yield self.env.timeout(duracao)

# Execução da simulação
ambiente = simpy.Environment()
# Cria um objeto de Car, adicionando a ele um environment. A partir disso,
# o ambiente já executará o objeto carro.
carro = Carro(ambiente)
ambiente.run(until = 200)