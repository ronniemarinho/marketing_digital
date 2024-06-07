import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Carregar os comentários do arquivo CSV
df_comentarios = pd.read_csv('tweet2.csv')

# Inicializar o analisador de sentimentos do VADER
analisador = SentimentIntensityAnalyzer()

# Inicializar listas para armazenar comentários positivos, negativos e neutros
comentarios_positivos = []
comentarios_negativos = []
comentarios_neutros = []

# Realizar a análise de sentimento dos comentários e armazenar os resultados
for comentario in df_comentarios['Comentario']:
    polaridade = analisador.polarity_scores(comentario)['compound']
    if polaridade > 0.05:
        comentarios_positivos.append(comentario)
    elif polaridade < -0.05:
        comentarios_negativos.append(comentario)
    else:
        comentarios_neutros.append(comentario)

# Contagem de comentários
total_positivos = len(comentarios_positivos)
total_negativos = len(comentarios_negativos)
total_neutros = len(comentarios_neutros)

# Gráfico de pizza para visualizar a distribuição dos sentimentos
labels = ['Positivos', 'Negativos', 'Neutros']
sizes = [total_positivos, total_negativos, total_neutros]
colors = ['lightgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0)  # Destacar a primeira fatia (positivos)

plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Mantém o aspecto do círculo
plt.title('Distribuição dos Sentimentos nos Comentários')
plt.show()

# Imprimir a quantidade de comentários positivos, negativos e neutros
print("Total de comentários positivos:", total_positivos)
print("Total de comentários negativos:", total_negativos)
print("Total de comentários neutros:", total_neutros)

# Imprimir os comentários neutros
print("\nComentários neutros:")
for comentario in comentarios_positivos:
    print(comentario)
