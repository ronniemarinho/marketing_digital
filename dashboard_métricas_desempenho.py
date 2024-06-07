import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# ccarregando os dados de desempenho do Google Ads (exemplo)
dados_desempenho = pd.read_csv('google_ads.csv')

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div(children=[
    html.H1(children='Dashboard de Desempenho do Google Ads', style={'textAlign': 'center', 'color': '#1a73e8', 'font-family': 'Arial, sans-serif', 'margin-bottom': '20px'}),

    # Métricas de desempenho
    html.Div(children=[
        html.Div(children=[
            html.H2('Cliques', style={'textAlign': 'center', 'color': '#1a73e8', 'font-family': 'Arial, sans-serif'}),
            html.H3(dados_desempenho['Cliques'].sum(), style={'textAlign': 'center', 'color': '#1a73e8', 'font-family': 'Arial, sans-serif', 'margin-top': '5px'})
        ], className='metric-box'),

        html.Div(children=[
            html.H2('Impressões', style={'textAlign': 'center', 'color': '#1a73e8', 'font-family': 'Arial, sans-serif'}),
            html.H3(dados_desempenho['Impressoes'].sum(), style={'textAlign': 'center', 'color': '#1a73e8', 'font-family': 'Arial, sans-serif', 'margin-top': '5px'})
        ], className='metric-box'),

        html.Div(children=[
            html.H2('Custo Total', style={'textAlign': 'center', 'color': '#1a73e8', 'font-family': 'Arial, sans-serif'}),
            html.H3('${:,.2f}'.format(dados_desempenho['Custo'].sum()), style={'textAlign': 'center', 'color': '#1a73e8', 'font-family': 'Arial, sans-serif', 'margin-top': '5px'})
        ], className='metric-box'),

        html.Div(children=[
            html.H2('CTR', style={'textAlign': 'center', 'color': '#1a73e8', 'font-family': 'Arial, sans-serif'}),
            html.H3('{:.2f}%'.format((dados_desempenho['Cliques'].sum() / dados_desempenho['Impressoes'].sum()) * 100), style={'textAlign': 'center', 'color': '#1a73e8', 'font-family': 'Arial, sans-serif', 'margin-top': '5px'})
        ], className='metric-box'),

        html.Div(children=[
            html.H2('CPC', style={'textAlign': 'center', 'color': '#1a73e8', 'font-family': 'Arial, sans-serif'}),
            html.H3('${:,.2f}'.format(dados_desempenho['Custo'].sum() / dados_desempenho['Cliques'].sum()), style={'textAlign': 'center', 'color': '#1a73e8', 'font-family': 'Arial, sans-serif', 'margin-top': '5px'})
        ], className='metric-box')
    ], className='metrics-container'),

    # Gráficos de desempenho
    html.Div(children=[
        html.Div(children=[
            dcc.Graph(
                id='cliques-impressoes',
                figure={
                    'data': [
                        go.Histogram(x=dados_desempenho['Cliques'], name='Cliques', marker_color='#1a73e8'),
                        go.Histogram(x=dados_desempenho['Impressoes'], name='Impressões', marker_color='#e3742f')
                    ],
                    'layout': {
                        'title': 'Histograma de Cliques vs Impressões',
                        'xaxis': {'title': 'Quantidade', 'tickfont': {'family': 'Arial, sans-serif'}, 'titlefont': {'family': 'Arial, sans-serif'}},
                        'yaxis': {'title': 'Frequência', 'tickfont': {'family': 'Arial, sans-serif'}, 'titlefont': {'family': 'Arial, sans-serif'}},
                        'plot_bgcolor': '#f9f9f9',
                        'paper_bgcolor': '#ffffff'
                    }
                }
            )
        ], className='chart-box'),

        html.Div(children=[
            dcc.Graph(
                id='custo-ctr',
                figure={
                    'data': [
                        go.Pie(labels=['Custo', 'CTR'], values=[dados_desempenho['Custo'].sum(), (dados_desempenho['Cliques'].sum() / dados_desempenho['Impressoes'].sum()) * 100], marker_colors=['#1a73e8', '#e3742f'])
                    ],
                    'layout': {
                        'title': 'Custo vs CTR (em %)',
                        'plot_bgcolor': '#f9f9f9',
                        'paper_bgcolor': '#ffffff'
                    }
                }
            )
        ], className='chart-box')
    ], className='charts-container')
], className='dashboard-container')

if __name__ == '__main__':
    app.run_server(debug=True)
