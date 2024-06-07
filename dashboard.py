import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
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

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div(children=[
    html.H1(children='Dashboard de Sentimento'),

    html.Div(children='''
        Distribuição dos Sentimentos nos Comentários:
    '''),

    # Gráfico de barras para a distribuição dos sentimentos
    dcc.Graph(
        id='sentimento-grafico',
        figure={
            'data': [
                {'x': ['Positivos', 'Negativos', 'Neutros'], 'y': [total_positivos, total_negativos, total_neutros], 'type': 'bar', 'name': 'Sentimentos'}
            ],
            'layout': {
                'title': 'Distribuição dos Sentimentos'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
