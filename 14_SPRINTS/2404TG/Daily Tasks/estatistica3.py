# -*- coding: utf-8 -*-
"""estatistica3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jJFQFcfv-2nuCGc1YV1taO6V_YKBYHBi
"""

#print = plt.show() para exibir o grafico.
#https://matplotlib.org/ site de graficos, copia e modifica

#exemplo do site
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data:
x = 0.5 + np.arange(8)
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="red", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

california_list = pd.read_csv('./sample_data/california_housing_train.csv')
print(california_list)

display(california_list.head(5))

#Fazer grafico e mudar nomes em inglês para português.

california_list.columns = ['longitude', 'latitude','media de idade','total de salas','total quartos','população','reservas','media','valor medio']
display(california_list.head(20))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x_t = 'Frogs', 'Hogs', 'Dogs', 'Logs'
y_d = [1,2,3,4]
df=pd.DataFrame({'x':x_t,
                'b':y_d},
                index=x_t)

print(df)
df.plot.barh(title='valores') #label eh o nome que vai aparecer no tronco

# Commented out IPython magic to ensure Python compatibility.
#exemplo modificado
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
# %matplotlib inline

fig, ax = plt.subplots(figsize=(5, 3))


fruits = ['apple', 'blueberry', 'cherry', 'orange','strawberry']
counts = [40, 100, 30, 55, 80]
bar_labels = ['green', 'purple', '_red', 'orange', 'blue']
bar_colors = ['tab:green', 'tab:purple', 'tab:red', 'tab:orange', 'tab:blue']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('\n fruit supply \n',fontsize=10)
ax.set_xlabel('\n fruit supply\n',fontsize=10)
ax.set_title('\n Fruit supply by kind and color \n',fontsize=10)
ax.legend(title='Fruit color', fontsize=8)


plt.show()



n = [[1,2,3,44], [4,5,6,55], [7,8,9,77], [10,20,30,99], [40,50,60,54]]
df=np.array(n)

print(df)

