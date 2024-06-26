# -*- coding: utf-8 -*-
"""Untitled49.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VjA6zLrbDCxPNnptcQZVZ_6kOmKAla0G
"""

import numpy as np

#Extração de linhas e colunas

l= np.array([[4,5,6],[6,1,7],[7,4,8]])

print(l)

print(l[2,1])

#Primeira linhas, todas as colunas
l_linha_1= l[0,:]

print(l_linha_1)

l_linha_2=l[1,:]

print(l_linha_2)

l_linha_3=l[2,:]

print(l_linha_3)

#todas as linhas, primeira coluna
l_coluna_1=l[:,0]

print(l_coluna_1)

#todas as linhas, segunda coluna
l_coluna_2=l[:,1]

print(l_coluna_2)

#Operações
n=np.array([[1,2],[3,4]])

print(n)

o= np.array([[1,1],[1,1]])

print(o)

res1=n+o

print(res1)

res2=n*o

print(res2)

p= np.array([[1,2],[3,4],[5,6]])

q= np.array([[2,1]])

print(q)

print(p+q)

#transposição, rearranjo de um conjunto
#de 15 elementos de 0 a 14
f=np.arange(15).reshape((3,5))

print(f)

#matriz transposta
s=f.transpose((1,0))

print(s)

#matriz aleatória com numeros positivos e negativos
v=np.random.randn(4,4)

print(v)

#Verifica na Array os valores booleanos
x=(v>0)

print(x)

#Criando a matriz com valores
#-1 e 1 baseados nos valores do array
z=np.where(x>0,1,-1)

print(z)