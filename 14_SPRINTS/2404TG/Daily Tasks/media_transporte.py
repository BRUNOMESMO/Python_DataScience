# -*- coding: utf-8 -*-
"""Media-transporte.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-8iDGIwvM-4IXr-3Btuu3-mmsZ_ysYPt
"""

import statistics as st

#Metro/trem/onibus/
dados= [30,60,90,60,50,150,30,105,105,30,7,90,60,45,80,60,50,150,30,105,105,30,50]

#media geral
media = st.mean(dados)

print(media)

#mediana geral
mediana = st.median(dados)

print(mediana)

desvio_padrao=st.stdev(dados)