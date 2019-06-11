def queue(env, resource, person, arrival, priority):
	yield env.timeout(arrival)
	print(person, 'arrived at', env.now)
	with resource.request(priority = priority) as res:
		yield res
		print(person, 'attended at', env.now)
		yield env.timeout(5)

import simpy

env = simpy.Environment()
resource = simpy.PriorityResource(env, capacity = 1)

env.process(queue(env, resource, 'Maria', 0, 2))
env.process(queue(env, resource, 'Paula', 1, 2))
env.process(queue(env, resource, 'Alana', 2, 0))

env.run()