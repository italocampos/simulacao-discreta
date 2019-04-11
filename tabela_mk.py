
# coding: utf-8

# In[1]:


data = [11 , 5 , 2 , 0 , 9 , 9 , 1 , 5 , 1 , 3 ,3 , 3 , 7 , 4 , 12 , 8 , 5 , 2 , 6 , 1 ,11 , 1 , 2 , 4 , 2 , 1 , 3 , 9 , 0 , 10 ,3 , 3 , 1 , 5 , 18 , 4 , 22 , 8 , 3 , 0 ,8 , 9 , 2 , 3 , 12 , 1 , 3 , 1 , 7 , 5 ,14 , 7 , 7 , 28 , 1 , 3 , 2 , 11 , 13 , 2 ,0 , 1 , 6 , 12 , 15 , 0 , 6 , 7 , 19 , 1 ,1 , 9 , 1 , 5 , 3 , 17 , 10 , 15 , 43 , 2 ,6 , 1 , 13 , 13 , 19 , 10 , 9 , 20 , 19 , 2 ,27 , 5 , 20 , 5 , 10 , 8 , 2 , 3 , 1 , 1 ,4 , 3 , 6 , 13 , 10 , 9 , 1 , 1 , 3 , 9 ,9 , 4 , 0 , 3 , 6 , 3 , 27 , 3 , 18 , 4 ,6 , 0 , 2 , 2 , 8 , 4 , 5 , 1 , 4 , 18 ,1 , 0 , 16 , 20 , 2 , 2 , 2 , 12 , 28 , 0 ,7 , 3 , 18 , 12 , 3 , 2 , 8 , 3 , 19 , 12 ,5 , 4 , 6 , 0 , 5 , 0 , 3 , 7 , 0 , 8 ,8 , 12 , 3 , 7 , 1 , 3 , 1 , 3 , 2 , 5 ,4 , 9 , 4 , 12 , 4 , 11 , 9 , 2 , 0 , 5 ,8 , 24 , 1 , 5 , 12 , 9 , 17 , 12 , 6 ,4 , 3 , 5 , 7 , 4 , 4 , 4 , 11 , 3 , 8]


# In[3]:


print(data)


# In[4]:


import math, statistics as st


# In[6]:


import matplotlib.pyplot as chart


# In[7]:


k = round(1 + 3.3 * math.log10(len(data)))


# In[8]:


chart.hist(data, bins=9)


# In[10]:


# Definindo lista com valores distintos de data
distinct = list(set(data))

# Ordenando os valores de distinct
distinct = sorted(distinct)


# In[11]:


print(distinct)


# In[12]:


# Contando as ocorrências dos valores de distinct em data
frequences = []
for value in distinct:
    frequences.append(data.count(value))


# In[25]:


# Calculando o valor de frequência acumulada
acc_freq = [frequences[0]]
for i in range(1, len(frequences)):
    acc_freq.append(acc_freq[i-1] + frequences[i])


# In[26]:


print(acc_freq)

