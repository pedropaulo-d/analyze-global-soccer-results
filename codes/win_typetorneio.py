# %%
import pandas as pd

df_matches = pd.read_csv('../data/Match_Results.csv', sep=',')

df_matches
# %%
def tipo_vitoria(row):
    if row['home_score'] > row['away_score']:  # Vitória do time da casa
        if row['neutral']:  # Se foi em campo neutro
            return 'Vitória em Campo Neutro'
        else:
            return 'Vitória em Casa'
    elif row['home_score'] < row['away_score']:  # Vitória do time visitante
        if row['neutral']:  # Se foi em campo neutro
            return 'Vitória em Campo Neutro'
        else:
            return 'Vitória Fora de Casa'
    else:
        return 'Empate'
    
df_matches['tipo_vitoria'] = df_matches.apply(tipo_vitoria, axis=1)

df_matches

# %%
def categoria_torneio(row):
    if row['tournament'] == 'FIFA World Cup qualification':
        return 'Eliminatórias da Copa do Mundo'
    
    elif row['tournament'] == 'FIFA World Cup':
        return 'Copa do Mundo'
    
    else:
        return 'Outros Torneios'
    
df_matches['tipo_torneio'] = df_matches.apply(categoria_torneio, axis=1)

df_matches

# %%
df_qtd_win = df_matches[df_matches['tipo_vitoria'] != 'Empate'].groupby(['tipo_torneio']).size().reset_index(name='total_vitorias')

df_qtd_win
# %%
import plotly.express as px


fig = px.bar(
            df_qtd_win, 
            x='tipo_torneio', 
            y='total_vitorias',
            color='tipo_torneio',
            title='Quantidade de Vitórias nos Torneios',
            labels={
                    'value': 'Número de Vitórias',
                    'variable': 'Tipo de Jogo',
                    'tipo_torneio': 'Torneio',
                    'total_vitorias': 'N° de Vitórias'
                    })
fig.show()