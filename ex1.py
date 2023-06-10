import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1
df = pd.read_csv('transferencias - 05_2023.csv')

# 2
df = df.drop("ANO / MÊS", axis='columns')
df['VALOR TRANSFERIDO'] = df['VALOR TRANSFERIDO'].str.replace(',', '.').astype(float)
print(df['VALOR TRANSFERIDO'])
print(type(df['VALOR TRANSFERIDO'][0]))

# 3
valorMax = np.max(df['VALOR TRANSFERIDO'])
valorMin = np.min(df['VALOR TRANSFERIDO'])
media = np.mean(df['VALOR TRANSFERIDO'])
print(f'Valor Máximo: {valorMax}')
print(f'Valor Mínimo: {valorMin}')
print(f'Valor Médio: {media}')

# 4
tipos_favorecidos = df['TIPO FAVORECIDO']
valor_transferido = df['VALOR TRANSFERIDO']
plt.bar(tipos_favorecidos, valor_transferido)
plt.xlabel('Tipo Favorecido')
plt.ylabel('Valor Transferido')
plt.title('Valores transferidos para cada tipo')
plt.show()
