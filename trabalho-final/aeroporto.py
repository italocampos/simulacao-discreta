import simpy
import scipy.stats as st
from random import randint

class Aviao:
    def __init__(self, env, nome, tipo, chegada, partida):
        self.env = env
        self.nome = nome
        self.tipo = tipo
        self.chegada = chegada
        self.partida = partida
        
class Aeroporto:
    def __init__(self, env, pistaPequena, pistaGrande, plataforma, hangar):
        self.env = env
        self.pistaPequena = pistaPequena
        self.pistaGrande = pistaGrande
        self.plataforma = plataforma
        self.hangar = hangar
    
    def aterrisar(self, aviao):
        yield self.env.timeout(aviao.chegada)
        print('Aeronave %s do tipo %d requisitou pista de aterrisagem em %d' % (aviao.nome, aviao.tipo , self.env.now))
        
        if aviao.tipo == 0:
            with self.pistaPequena.request() as req:
                yield req
                print('Aeronave %s do tipo %d iniciou aterrisagem em %d' % (aviao.nome, aviao.tipo , self.env.now))
                yield self.env.timeout(10)
        else:
            with self.pistaGrande.request() as req:
                print('Aeronave %s do tipo %d iniciou aterrisagem em %d' % (aviao.nome, aviao.tipo , self.env.now))
                yield req
                yield self.env.timeout(20)
                
        print('Aeronave %s do tipo %d finalizou aterrisagem em %d' % (aviao.nome, aviao.tipo , self.env.now))
        self.env.process(self.desembarque(aviao))
        
    def desembarque(self, aviao):
        with self.plataforma.request() as req:
            yield req
            print('Aeronave %s do tipo %d iniciou desembarque em %d' % (aviao.nome, aviao.tipo , self.env.now))
            if aviao.tipo == 0:
                yield self.env.timeout(15)
            else:
                yield self.env.timeout(30)
        
        print('Aeronave %s do tipo %d finalizou desembarque em %d' % (aviao.nome, aviao.tipo , self.env.now))
        self.env.process(self.estacionar(aviao))

    def estacionar(self, aviao):
        with self.hangar.request() as req:
            yield req
            print('Aeronave %s do tipo %d estacionou em um hangar em %d' % (aviao.nome, aviao.tipo , self.env.now))
            yield self.env.timeout(aviao.partida)
        
        print('Aeronave %s do tipo %d saiu do hangar em %d' % (aviao.nome, aviao.tipo , self.env.now))
        self.env.process(self.embarque(aviao))

    def embarque(self, aviao):
        with self.plataforma.request() as req:
            yield req
            print('Aeronave %s do tipo %d iniciou embarque em %d' % (aviao.nome, aviao.tipo , self.env.now))
            if aviao.tipo == 0:
                yield self.env.timeout(15)
            else:
                yield self.env.timeout(30)
        
        print('Aeronave %s do tipo %d finalizou embarque em %d' % (aviao.nome, aviao.tipo , self.env.now))
        self.env.process(self.decolar(aviao))
    
    def decolar(self, aviao):
        print('Aeronave %s do tipo %d preparada para decolagem em %d' % (aviao.nome, aviao.tipo , self.env.now))
        
        if aviao.tipo == 0:
            with self.pistaPequena.request() as req:
                yield req
                print('Aeronave %s do tipo %d iniciou decolagem em %d' % (aviao.nome, aviao.tipo , self.env.now))
                yield self.env.timeout(10)
        else:
            with self.pistaGrande.request() as req:
                yield req
                print('Aeronave %s do tipo %d iniciou decolagem em %d' % (aviao.nome, aviao.tipo , self.env.now))
                yield self.env.timeout(20)
        
        print('Aeronave %s do tipo %d decolou em %d' % (aviao.nome, aviao.tipo , self.env.now))
    
    
env = simpy.Environment()

aeronaves = [Aviao(env, 'AV321-PA', 0, 0, 40),
    Aviao(env, 'AV155-MA', 1, 20, 60),
    Aviao(env, 'QR382-MT', 1, 167, 237),
    Aviao(env, 'SD348-SP', 0, 239, 314),
    Aviao(env, 'AC111-AC', 1, 269, 469),
    Aviao(env, 'DF879-CE', 1, 274, 489),
    Aviao(env, 'ZX422-PI', 1, 399, 629),
    Aviao(env, 'NN228-RJ', 0, 414, 719),
    Aviao(env, 'GF483-SP', 0, 429, 744),
    Aviao(env, 'DE322-MG', 1, 439, 759),
    ]

'''
nomes = ['AV321-PA', 'AV155-MA', 'QR382-MT', 'SD348-SP', 'AC111-AC', 'DF879-CE', 'ZX422-PI', 'NN228-RJ', 'GF483-SP', 'DE322-MG']
aeronaves = []
chegadas = list(st.expon.rvs(size = len(nomes), loc = 0, scale = 15))
partidas = list(st.expon.rvs(size = len(nomes), loc = 0, scale = 15))

# Cria e incializa dos vetores de valores de chegadas e partidas
chegadas_acc, partidas_acc = [chegadas[0]], [partidas[0]]
# Acumula os tempos de chegada e partida
for i in range(1, len(chegadas)):
    chegadas_acc.append(chegadas_acc[i-1] + chegadas[i])
    partidas_acc.append(partidas_acc[i-1] + partidas[i])

# Soma os tempos acumulados de chegadas e partidas para se obter o 
# tempo que a aeronave sai do hangar
for i in range(len(partidas)):
    partidas_acc[i] = chegadas_acc[i] + partidas_acc[i]

# Faz a lista de objetos
for i in range(len(nomes)):
    aeronaves.append(Aviao(env, nomes[i], randint(0, 1), int(chegadas_acc[i]), int(partidas_acc[i])))

#print('chegadas:', chegadas_acc)
#print('partidas:', partidas_acc)
'''

pistaPequena = simpy.Resource(env, capacity=2)
pistaGrande = simpy.Resource(env, capacity=2)
plataforma = simpy.Resource(env, capacity=5)
hangar = simpy.Resource(env, capacity=7)

aero = Aeroporto(env, pistaPequena, pistaGrande, plataforma, hangar)

for aviao in aeronaves:
    env.process(aero.aterrisar(aviao))

env.run()
