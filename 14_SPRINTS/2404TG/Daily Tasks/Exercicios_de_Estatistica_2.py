# -*- coding: utf-8 -*-
"""trabalhoEmGrupo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VR2dpayDGzrVDB3XH8TdRJboiWGNyXXT
"""

import statistics as st

tempoLista = []
transporteLista = []

while True:
  tempo = int(input('Digite o tempo: '))

  if tempo == 0:
    break

  tempoLista.append(tempo)
  transporte = str(input('Digite o transporte: '))
  transporteLista.append(transporte)

media = st.mean(tempoLista)
mediana = st.median(tempoLista)
moda = st.mode(tempoLista)
desvioPadrao = st.stdev(tempoLista)

print(transporteLista)
print(f'Está sera o tempo medio: {media:.2f} minutos para chegada a escola')
print(f'Está sera a mediana: {mediana:.2f} minutos dos alunos a chegada a escola')
print(f'Está sera a moda: {moda:.2f} minutos do tempo aos alunos')
print(f'Desvio padrão: {desvioPadrao:.2f} do tempo dos alunos')