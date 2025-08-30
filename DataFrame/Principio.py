import pandas as pd
import numpy as np #Biblioteca para buscar a média

array = [80,85,90,95,100,105,110,115,120,125]

# DataFrame
d = {'cool': [1,2,3,4,7]
    ,'cool2': [4,5,6,9,5]
    ,'cool3': [7,8,12,1,11]}

# Descobrir quantas linhas ou colunas contém no DataFrame
df = pd.DataFrame(data=d)
print(df)
print("O DataFrame tem",df.shape[0],"linhas e",df.shape[1],"colunas")

#  Encontrar o maior valor dentro do array
max_value = max(array)
print("O maior valor do Array é:",max_value)

# Encontrar a média
mean_value = np.mean(array)
print(mean_value)