# -*- coding: utf-8 -*-
"""palavraInvertida.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10AbELG9rbBPyTbpmSONrpZSDquPFZRn8
"""

palavra = input("Digite uma palavra: ")

palavra_invertida = ''

for letra in palavra:
    palavra_invertida = letra + palavra_invertida

print("Palavra invertida:", palavra_invertida)