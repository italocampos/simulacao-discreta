# Third one simulation:
# - Managing interruptions;

import simpy
from random import randint

class Car(object):
	def __init__(self, environment):
		self.env = environment
		# Executa o método run toda vez que uma instância é criada
		self.action = environment.process(self.run())

	def run(self):
		while True:
			print('The car is parking and charging at {}'.format(self.env.now))
			charge_duration = 20
			# Durante o processo de carga (yelding um processo), podemos ter
			# uma interrupção
			try:
				yield self.env.process(self.charge(charge_duration))
			except simpy.Interrupt:
				# Quando uma interrupção é recebida, pode-se gerenciar isso
				# nesse try except
				print('# There was an interruption at charging process. :(')

			# O processo charge() terminou ou foi interrompido e o carro 
			# voltará a andar
			print('Start Driving at {}'.format(environment.now))
			drive_duration = randint(10,50)
			try:
				yield self.env.timeout(drive_duration)
			except simpy.Interrupt:
				print('# The car stopped abruptly at time {}'.format(self.env.now))

	def charge(self, duration):
		yield self.env.timeout(duration)

# Essa função pode ser interpretada como um novo processo que 
# lança uma interrupção para o objeto car, já que possui uma
# referência a esse objeto.
def driver(env, car):
	while True:
		yield env.timeout(randint(5,20))
		car.action.interrupt()

# Execução da simulação
environment = simpy.Environment()
# Cria um objeto de Car, adicionando a ele um environment. A partir disso,
# o ambiente já executará o objeto car.
car = Car(environment)
# Instância do processo driver (adiciona-o ao environment)
environment.process(driver(environment, car))
environment.run(until = 200)