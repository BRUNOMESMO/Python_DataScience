# -*- coding: utf-8 -*-
"""PositivoENegativoComFuncao1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EyLfy4oS-5inIhDs6Stf-cfuXEgfaoYd
"""

def estado(numero):
  if numero > 0:
    print('P')
    return True
  else:
    print('N')
    return True

while True:
  numero = int(input('Digite um caractere: '))
  if estado(numero):
    break