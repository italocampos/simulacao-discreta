import simpy, numpy, scipy.stats as st

def queue(env, resource, person, arrival):
	yield env.timeout(arrival)
	with resource.request() as res:
		yield res
		print(person, 'attended at', env.now)
		yield env.timeout(5)

env = simpy.Environment()
resource = simpy.Resource(env, capacity = 1)

numpy.random.seed(51)
p = st.expon.rvs(size = 10, loc = 0, scale = 3)

# Acumula os tempos de chegada das pessoas na fila
for i in range(1, len(p)):
	p[i] += p[i-1]

for i in range(len(p)):
	env.process(queue(env, resource, 'Pessoa %d' %i, p[i]))

env.run()