# -*- coding: utf8 -*-

class Oficina:
	def __init__(self, ambiente):
		self.ambiente = ambiente
		self.mecanico_disponivel = self.ambiente.event()
		self.ambiente.process(self.chegou_carro())
		self.ambiente.process(self.chegou_mecanico())

	def chegou_carro(self):
		yield self.mecanico_disponivel
		print('Reparos iniciados em', self.ambiente.now)

	def chegou_mecanico(self):
		yield self.ambiente.timeout(13)
		self.mecanico_disponivel.succeed()
		yield self.ambiente.timeout(1)
		print('Mecânico disponível em', self.ambiente.now)

import simpy
ambiente = simpy.Environment()
Oficina(ambiente)
ambiente.run()