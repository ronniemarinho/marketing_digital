# Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Carregamento dos dados
dados = pd.read_csv('dados_clientes2.csv')

# Visualização das primeiras linhas do conjunto de dados
print(dados.head())

# Pré-processamento dos dados
X = dados.drop(['clienteid', 'email'], axis=1)  # Removendo o identificador do cliente e o e-mail
print(X)
# padronização é útil quando as variáveis ​​dos seus dados estão em diferentes escalas ou têm diferentes unidades de medida.
# Isso pode afetar a precisão e o desempenho dos algoritmos de clusterização, como o K-means, porque eles são sensíveis às escalas
# dos dados.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Padronizando os dados
print('padronizados')
print(X_scaled)

# Aplicação do algoritmo K-means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)
labels = kmeans.labels_
print('labelss',labels)#labelss [1 2 1 2 2 2 0 2 2 2 0 2 0 2 1 1 1

# Adicionando os rótulos de cluster aos dados
dados['Cluster'] = labels
print('dados')
print(dados)

# Salvando os registros de cada grupo em arquivos CSV
for i in range(kmeans.n_clusters):
    cluster_data = dados[dados['Cluster'] == i]#realiza uma operação de filtragem nos dados armazenados no DataFrame dados. Ela cria um novo DataFrame chamado cluster_data, que contém apenas as linhas em que o valor da coluna 'Cluster' é igual a i
    #print('clusss', cluster_data)
    cluster_data.to_csv(f'cluster_{i}_dados.csv', index=False)

# Imprimindo uma mensagem indicando que os arquivos foram salvos com sucesso
print("Arquivos CSV dos registros de cada grupo salvos com sucesso!")

# Visualização dos clusters
#cmap='viridis': Este parâmetro define o mapa de cores a ser usado para mapear os valores numéricos dos clusters para cores.
# 'viridis' é um mapa de cores pré-definido que varia de azul a amarelo.
plt.scatter(dados['idade'], dados['renda_anual'], c=dados['Cluster'], cmap='viridis')
plt.xlabel('idade')
plt.ylabel('renda_anual')
plt.title('Segmentação de Mercado - Clusters de Clientes')
plt.show()

'''
# Visualização dos centros dos clusters
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
plt.xlabel('idade')
plt.ylabel('renda_anual')
plt.title('Centros dos Clusters')
plt.show()
'''