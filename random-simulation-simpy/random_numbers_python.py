# Gerando distribuições de números aleatórios em Python

import scipy.stats as st
import matplotlib.pyplot as chart
import math

# Distribuição unifome
conjunto = st.uniform.rvs(size=2000, loc=75, scale=2)
''' 
> 'loc' significa que os números aleatórios serão gerados a 
partir de 'loc' 
> 'scale' diz respeito à variação dos valores gerados pela
função de geração de números aleatórios
> 'size' está relacionado com o valor padrão de geração de
números aleatórios
'''
k = round(3.3 * math.log10(2000))
chart.hist(conjunto, bins=k)
chart.show()

# Distribuição exponencial
conjunto = st.expon.rvs(size = 200, loc = 75, scale = 2)
k = round(3.3 * math.log10(200))
chart.hist(conjunto, bins=k)
chart.show()

# Distribuição normal (Gaussiana)
conjunto = st.norm.rvs(size = 100, loc = 75)
k = round(3.3 * math.log10(100))
chart.hist(conjunto, bins=k)
chart.show()

# Distribuição log-normal
conjunto = st.lognorm.rvs(s = 0.945, size = 2000, loc = 75)
k = round(3.3 * math.log10(2000))
chart.hist(conjunto, bins=k)
chart.show()

# Distribuição triangular
conjunto = st.triang.rvs(c = 0.158, size = 2000, loc = 75)
k = round(3.3 * math.log10(2000))
chart.hist(conjunto, bins=k)
chart.show()

# Ajustando semente no scipy
numpy.random.seed(20)