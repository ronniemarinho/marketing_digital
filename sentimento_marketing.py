# Importações de Bibliotecas
import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib para visualização de dados
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  # Importa o analisador de sentimentos do VADER

# Carregar os comentários do arquivo CSV
df_comentarios = pd.read_csv('tweet2.csv')  # Carrega os comentários do arquivo CSV 'tweet2.csv' em um DataFrame

# Inicializar o analisador de sentimentos do VADER
analisador = SentimentIntensityAnalyzer()  # Inicializa o analisador de sentimentos do VADER

# Inicializar listas para armazenar comentários positivos, negativos e neutros
comentarios_positivos = []  # Inicializa uma lista para armazenar comentários positivos
comentarios_negativos = []  # Inicializa uma lista para armazenar comentários negativos
comentarios_neutros = []  # Inicializa uma lista para armazenar comentários neutros

# Realizar a análise de sentimento dos comentários e armazenar os resultados
for comentario in df_comentarios['Comentario']:  # Itera sobre cada comentário no DataFrame
    polaridade = analisador.polarity_scores(comentario)['compound']  # Calcula a polaridade do sentimento do comentário
    if polaridade > 0.05:  # Se a polaridade for positiva
        comentarios_positivos.append(comentario)  # Adiciona o comentário à lista de comentários positivos
    elif polaridade < -0.05:  # Se a polaridade for negativa
        comentarios_negativos.append(comentario)  # Adiciona o comentário à lista de comentários negativos
    else:  # Se a polaridade for neutra
        comentarios_neutros.append(comentario)  # Adiciona o comentário à lista de comentários neutros

# Contagem de comentários
total_positivos = len(comentarios_positivos)  # Calcula o total de comentários positivos
total_negativos = len(comentarios_negativos)  # Calcula o total de comentários negativos
total_neutros = len(comentarios_neutros)  # Calcula o total de comentários neutros

# Gráfico de pizza para visualizar a distribuição dos sentimentos
plt.figure(figsize=(10, 5))  # Define o tamanho da figura do gráfico
plt.subplot(1, 2, 1)  # Cria um subplot para o gráfico de pizza
labels = ['Positivos', 'Negativos', 'Neutros']  # Rótulos para as fatias do gráfico
sizes = [total_positivos, total_negativos, total_neutros]  # Tamanhos das fatias do gráfico
colors = ['lightgreen', 'lightcoral', 'lightskyblue']  # Cores das fatias do gráfico
explode = (0.1, 0, 0)  # Destaca a primeira fatia (positivos)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)  # Cria o gráfico de pizza
plt.axis('equal')  # Mantém o aspecto do círculo
plt.title('Distribuição dos Sentimentos nos Comentários')  # Define o título do gráfico

# Gráfico de barras para visualizar a distribuição dos sentimentos
plt.subplot(1, 2, 2)  # Cria um subplot para o gráfico de barras
sentimentos = ['Positivos', 'Negativos', 'Neutros']  # Sentimentos
quantidades = [total_positivos, total_negativos, total_neutros]  # Quantidades
plt.bar(sentimentos, quantidades, color=['lightgreen', 'lightcoral', 'lightskyblue'])  # Cria o gráfico de barras
plt.title('Distribuição dos Sentimentos nos Comentários')  # Define o título do gráfico
plt.ylabel('Quantidade')  # Rótulo do eixo y

plt.tight_layout()  # Ajusta o layout para evitar sobreposição
plt.show()  # Mostra os gráficos

# Imprimir a quantidade de comentários positivos, negativos e neutros
print("Total de comentários positivos:", total_positivos)  # Imprime o total de comentários positivos
print("Total de comentários negativos:", total_negativos)  # Imprime o total de comentários negativos
print("Total de comentários neutros:", total_neutros)  # Imprime o total de comentários neutros

# Imprimir os comentários neutros
print("\nComentários neutros:")  # Imprime um título para os comentários neutros
for comentario in comentarios_positivos:  # Itera sobre os comentários positivos
    print(comentario)  # Imprime cada comentário positivo
