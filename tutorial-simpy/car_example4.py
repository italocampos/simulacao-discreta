# Fourth one simulation:
# - Resource usage;

import simpy

def car(environment, name, bcs, driving_time, charge_duration):
	# Driving to the BCS (posto de carga)
	yield environment.timeout(driving_time)

	# Request one of BCS charging spots
	print('%s arriving to the BCS spot at %d' % (name, environment.now))
	with bcs.request() as req:
		yield req

		# Charge the battery
		print('%s is charging its battery at %d' % (name, environment.now))
		yield environment.timeout(charge_duration)
		print('%s is leaving the BCS at %d' % (name, environment.now))


# Starting the simulation
env = simpy.Environment()
# Creating a resource and referecing to the environment
bcs = simpy.Resource(env, capacity = 2)
# Creating the car process
for i in range(4):
	env.process(car(env, 'Car %d' % i, bcs, i*2, 6))
# run() don't have arguments because the car processes have a defined end
env.run()