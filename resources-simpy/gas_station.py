# Classes definition
class Car:
	def __init__(self, env, model, arrival, fill_time, fuel_level):
		self.env = env
		self.model = model
		self.arrival = arrival
		self.fill_time = fill_time
		self.fuel_level = fuel_level

class GasStation:
	def __init__(self, env, pumps, tank):
		self.env = env
		self.pumps = pumps
		self.tank = tank

	def fill_up(self, car):
		yield self.env.timeout(car.arrival)
		print(car.model, 'arrived at', self.env.now)
		with self.pumps.request() as pump:
			yield pump
			print(car.model, 'started the filling at', self.env.now)
			yield self.tank.get(car.fuel_level)
			print('Tanque com %d litros' % (self.tanque.level))
			yield self.env.timeout(carro.tempo_abastecimento)
			print(carro.nome, 'saiu do abastecimento em', self.env.now)

			if self.tanque.level < 50:
				print('Chama caminhão de combustível em', self.env.now)
				self.env.process(self.reabastece())
				yield self.env.timeout(5)

# Simulation startup
import simpy
env = simpy.Environment()

car_1 = Car(env, 'Fiat Uno', 5, 3)
car_2 = Car(env, 'Ford Ka', 0, 3)
car_3 = Car(env, 'Renault Kwid', 7, 3)
car_4 = Car(env, 'Volksvagen Gol', 2, 3)
car_5 = Car(env, 'Chevrolet Agile', 6, 3)

pump = simpy.Resource(env, capacity = 1)
tank = simpy.Container(env, capacity = 100, init = 100)
gas_station = GasStation(env, pump, tank)

env.process(gas_station.fill_up(car_1))
env.process(gas_station.fill_up(car_2))
env.process(gas_station.fill_up(car_3))
env.process(gas_station.fill_up(car_4))
env.process(gas_station.fill_up(car_5))

env.run()