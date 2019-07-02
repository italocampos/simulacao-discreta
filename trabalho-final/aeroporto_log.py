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
        self.log = "AERONAVE: %s | TIPO: %d\n" % (self.nome, self.tipo)
        
class Aeroporto:
    def __init__(self, env, pistaPequena, pistaGrande, plataforma, hangar):
        self.env = env
        self.pistaPequena = pistaPequena
        self.pistaGrande = pistaGrande
        self.plataforma = plataforma
        self.hangar = hangar
    
    def aterrissar(self, aviao):
        yield self.env.timeout(aviao.chegada)
        aviao.log += 'Requisitou pista de aterrissagem em %d\n' % self.env.now
        
        if aviao.tipo == 0:
            with self.pistaPequena.request() as req:
                yield req
                aviao.log += 'Iniciou aterrissagem em %d\n' % self.env.now
                yield self.env.timeout(10)
        else:
            with self.pistaGrande.request() as req:
                yield req
                aviao.log += 'Iniciou aterrissagem em %d\n' % self.env.now
                yield self.env.timeout(20)

        aviao.log += 'Finalizou aterrissagem em %d\n' % self.env.now
        self.env.process(self.desembarque(aviao))
        
    def desembarque(self, aviao):
        with self.plataforma.request() as req:
            aviao.log += 'Aeronave aguarda por plataforma de desembarque em %d\n' % self.env.now
            yield req
            aviao.log += 'Iniciou desembarque em %d\n' % self.env.now
            if aviao.tipo == 0:
                yield self.env.timeout(15)
            else:
                yield self.env.timeout(30)
        
        aviao.log += 'Finalizou desembarque em %d\n' % self.env.now
        self.env.process(self.estacionar(aviao))

    def estacionar(self, aviao):
        with self.hangar.request() as req:
            yield req
            aviao.log += 'Estacionou em hangar em %d\n' % self.env.now
            yield self.env.timeout(aviao.partida)
        
        aviao.log += 'Deixou o hangar em %d\n' % self.env.now
        self.env.process(self.embarque(aviao))

    def embarque(self, aviao):
        with self.plataforma.request() as req:
            aviao.log += 'Aeronave aguarda por plataforma de embarque em %d\n' % self.env.now
            yield req
            aviao.log += 'Iniciou embarque em %d\n' % self.env.now
            if aviao.tipo == 0:
                yield self.env.timeout(30)
            else:
                yield self.env.timeout(45)
        
        aviao.log += 'Finalizou o embarque em %d\n' % self.env.now
        self.env.process(self.decolar(aviao))
    
    def decolar(self, aviao):
        aviao.log += 'Aeronave preparada para decolagem em %d\n' % self.env.now
        
        if aviao.tipo == 0:
            with self.pistaPequena.request() as req:
                yield req
                aviao.log += 'Iniciou decolagem em %d\n' % self.env.now
                yield self.env.timeout(10)
        else:
            with self.pistaGrande.request() as req:
                yield req
                aviao.log += 'Iniciou decolagem em %d\n' % self.env.now
                yield self.env.timeout(20)
        
        aviao.log += 'Aeronave decolou em %d\n' % self.env.now
    
    
env = simpy.Environment()
'''
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

'''
aeronaves = []
chegadas = list(st.expon.rvs(size = len(nomes), loc = 0, scale = 50))
partidas = list(st.expon.rvs(size = len(nomes), loc = 0, scale = 50))

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
    aeronaves.append(Aviao(env, nomes[i], 1, int(round(chegadas_acc[i])), int(round(partidas_acc[i]))))

#print('chegadas:', chegadas_acc)
#print('partidas:', partidas_acc)
'''

# Dados da simulação
names = ['AV321-PA', 'AV155-MA', 'QR382-MT', 'SD348-SP', 'AC111-AC', 'DF879-CE', 'ZX422-PI', 'NN228-RJ', 'GF483-SP', 'DE322-MG',
    'JI455-RS', 'KP322-SE', 'OP544-PR', 'UT677-MS', 'JT877-TO', 'JI639-OJ', 'WT429-OC', 'QE002-LO', 'EN656-VR', 'QN857-NT', 
    'NH064-HB', 'OD519-OY', 'DX949-LX', 'AZ133-HK', 'SN933-VH', 'DA200-UM', 'LW181-SS', 'GT352-DO', 'GU849-TL', 'IN617-LO', 
    'YF283-DF', 'EX505-PN', 'TV053-GB', 'WU814-KK', 'UE675-VP', 'FE209-LY', 'XF439-KN', 'AE382-YO', 'NG643-SD', 'WK797-JE', 
    'XB390-QU', 'JV964-JH', 'ZM425-BD', 'AX609-PK', 'IM810-LZ', 'YN897-QI', 'JF647-KT', 'JK542-ML', 'QT627-CC', 'NW847-EJ', 
    'UQ442-IM', 'QN203-TK', 'RJ266-GO', 'MQ100-AZ', 'KN732-VC', 'DB410-CZ', 'FF329-EB', 'HJ628-IB', 'PE124-UT', 'XM231-LD', 
    'HN261-RV', 'MS855-PZ', 'CY238-QB', 'KF444-PM', 'ZM774-UM', 'BI473-AH', 'UF632-PL', 'HW812-EJ', 'FC428-AH', 'UL173-EN', 
    'LW861-FZ', 'QW038-NO', 'SY554-RY', 'NP121-OQ', 'BK631-QO', 'DF930-ZT', 'ER402-ZZ', 'MG466-RI', 'TI417-OS', 'UC859-TH', 
    'AE791-BO', 'SU683-YP', 'VX161-RC', 'UI461-XZ', 'HY809-OY', 'YB515-IN', 'RA648-RX', 'VN460-KU', 'IW196-LR', 'GY400-AU', 
    'CA137-TZ', 'ZE238-BF', 'KP432-AR', 'PQ308-MP', 'DF610-IU', 'LL084-QE', 'QM502-EN', 'IW501-BZ', 'SB616-XK', 'TO153-AE', 
    'VW244-EB', 'KD526-NC', 'SH489-KN', 'ZT163-PS', 'YA303-GC', 'WX399-ZM', 'BY740-VK', 'OJ883-YD', 'BU170-RN', 'VW481-VF', 
    'UQ798-ST', 'EL715-GQ', 'ET655-SD', 'WC277-IR', 'ID425-GC', 'KJ990-UT', 'VD354-TX', 'UW982-JN', 'VP152-QN', 'HI504-DR', 
    'UI169-GX', 'IA876-OY', 'EL376-HE', 'GA479-DJ', 'MY974-OQ', 'SV152-WD', 'FD034-YS', 'BJ841-XP', 'HJ045-SY', 'YP795-MF', 
    'LQ436-HD', 'XX531-QP', 'NB252-WV', 'OU132-MI', 'NI894-LS', 'IL856-XK', 'BX107-BG', 'WZ541-BK', 'IP961-NV', 'IP952-QR', 
    'BW433-UU', 'DV646-WA', 'JI808-KT', 'NS024-SW', 'MN592-WZ', 'GB214-RL', 'MV326-AB', 'BC813-JO', 'MF411-TI', 'OK672-UZ', 
    'VY388-AP', 'BV939-CM', 'PU508-BZ', 'NE554-JW', 'UR303-OZ', 'OK831-XG', 'TK303-OA', 'WY466-VF', 'TV061-DZ', 'JR214-CB', 
    'SE895-JX', 'IB635-AV', 'IE242-DY', 'VG528-PP', 'FR543-LR', 'HQ684-VU', 'PR447-JT', 'YI192-YK', 'LO432-RS', 'XC744-GN', 
    'YK297-ZT', 'CD974-TS', 'IR998-HC', 'KD749-HB', 'NG673-ZD', 'SH248-AH', 'QT560-VM', 'JA010-IN', 'RM522-PA', 'WW496-MR', 
    'ES471-VW', 'SK539-ZL', 'KH713-HJ', 'IO504-XS', 'GT684-BW', 'QX366-KT', 'NW072-UR', 'QD761-VT', 'NX323-VL', 'XR223-UC', 
    'IR574-OQ', 'QN728-DJ', 'CW054-WS', 'GG364-XH', 'YJ614-IF', 'WD618-LU', 'IQ687-LW', 'WH748-PL', 'PI407-IU', 'EX165-MX']

arrivals = [13, 174, 290, 379, 530, 550, 567, 584, 629, 631, 847, 857, 881, 886, 886, 904, 1088, 1102, 1146, 1187, 1212, 1267, 
1306, 1357, 1415, 1475, 1482, 1524, 1534, 1543, 1559, 1570, 1570, 1646, 1667, 1695, 1776, 1905, 1990, 2006, 2024, 2037, 2091, 
2183, 2262, 2334, 2358, 2359, 2361, 2371, 2391, 2395, 2409, 2411, 2414, 2603, 2603, 2612, 2746, 2768, 2804, 2805, 2840, 2946, 
2962, 3000, 3029, 3131, 3206, 3216, 3241, 3298, 3313, 3344, 3346, 3426, 3541, 3578, 3610, 3652, 3729, 3797, 3798, 3813, 3822, 
3842, 3893, 3928, 3946, 3978, 4055, 4113, 4129, 4150, 4205, 4239, 4377, 4402, 4464, 4527, 4561, 4634, 4643, 4831, 4873, 4909, 
4988, 4992, 5076, 5178, 5183, 5215, 5314, 5316, 5395, 5432, 5438, 5439, 5489, 5491, 5672, 5689, 5733, 5751, 5774, 5788, 5825, 
5830, 5840, 5883, 5893, 5975, 5977, 5999, 6033, 6078, 6093, 6113, 6234, 6243, 6251, 6298, 6353, 6368, 6373, 6429, 6600, 6628, 
6635, 6641, 6647, 6712, 6754, 6807, 6856, 6935, 6995, 7108, 7177, 7186, 7204, 7215, 7245, 7310, 7341, 7435, 7460, 7582, 7661, 
7695, 7738, 7774, 7877, 7953, 8033, 8077, 8109, 8110, 8181, 8214, 8270, 8296, 8454, 8573, 8655, 8728, 8763, 8795, 9008, 9114, 
9308, 9394, 9406, 9577, 9621, 9639, 9718, 9746, 9803, 9815]
 
hangar_time = [49, 35, 82, 44, 39, 87, 64, 60, 72, 36, 41, 43, 63, 59, 59, 79, 82, 61, 64, 59, 32, 38, 42, 29, 79, 90, 31, 46, 
100, 52, 29, 68, 124, 59, 144, 28, 74, 173, 67, 89, 49, 57, 81, 40, 71, 78, 44, 56, 73, 85, 21, 123, 50, 41, 15, 30, 37, 78, 
92, 88, 84, 89, 26, 44, 23, 67, 161, 14, 42, 19, 24, 32, 104, 81, 44, 103, 112, 25, 77, 22, 62, 67, 55, 46, 92, 145, 105, 47, 
62, 120, 84, 95, 73, 91, 167, 50, 55, 65, 95, 80, 75, 80, 60, 79, 60, 76, 29, 27, 23, 72, 105, 39, 131, 20, 24, 64, 101, 42, 
35, 94, 90, 46, 27, 36, 51, 123, 74, 143, 84, 38, 62, 112, 74, 23, 28, 97, 16, 28, 71, 27, 27, 49, 37, 112, 39, 120, 54, 119, 
79, 34, 69, 27, 79, 71, 36, 91, 207, 25, 66, 85, 26, 52, 21, 37, 39, 99, 26, 42, 46, 44, 73, 80, 47, 107, 29, 63, 68, 25, 20, 
29, 101, 73, 245, 17, 56, 226, 103, 39, 164, 55, 57, 29, 69, 37, 113, 30, 79, 55, 166, 124]
 
flight_types = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 
1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 
1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 
1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1]


# Lista com objetos da classe Aviao
flights = []
for i in range(len(names)):
    flights.append(Aviao(env, names[i], flight_types[i], arrivals[i], hangar_time[i]))

pistaPequena = simpy.Resource(env, capacity=2)
pistaGrande = simpy.Resource(env, capacity=1)
plataforma = simpy.Resource(env, capacity=5)
hangar = simpy.Resource(env, capacity=3)

aero = Aeroporto(env, pistaPequena, pistaGrande, plataforma, hangar)

for aviao in flights:
    env.process(aero.aterrissar(aviao))

env.run()

for aviao in flights:
    print(aviao.log)
    print('----------------------------------------------------')