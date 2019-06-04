# -*- coding: utf8 -*-

class Antissocial:
	def __init__(self, ambiente, tempo_game, tempo_ligacao):
		self.ambiente = ambiente
		self.tempo_ligacao = tempo_ligacao
		self.tempo_game = tempo_game
		self.zerou = self.ambiente.event()
		self.chamado = self.ambiente.event()
		self.ambiente.process(self.decide_sair())
		self.ambiente.process(self.video_game())
		self.ambiente.process(self.chamada())

	def decide_sair(self):
		yield self.zerou | self.chamado
		print('Saindo em', self.ambiente.now)

	def video_game(self):
		yield self.ambiente.timeout(self.tempo_game)
		self.zerou.succeed()
		#self.chamado.interrupt('Não vou esperar chamadas.')
		print('Jogando em', self.ambiente.now)

	def chamada(self):
		yield self.ambiente.timeout(self.tempo_ligacao)
		self.chamado.succeed()
		#processo = self.ambiente.process(self.zerou)
		#self.zerou.interrupt('Vou parar de jogar pra sair com os brothers.')
		print('Recebi chamada em', self.ambiente.now)

import simpy
ambiente = simpy.Environment()
Antissocial(ambiente, 13, 5)
ambiente.run()