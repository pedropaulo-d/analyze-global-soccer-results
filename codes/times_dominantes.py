# %%
import pandas as pd

df_matches = pd.read_csv('../data/Match_Results.csv', sep=',')

df_matches
# %%
def tipo_vitoria(row):
    if row['home_score'] > row['away_score']:  # Vitória do time da casa
        return row['away_team']
        
    elif row['home_score'] < row['away_score']:  # Vitória do time visitante
        return row['away_team']
    else:
        return 'Empate'
    
df_matches['time_ganhador'] = df_matches.apply(tipo_vitoria, axis=1)

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
condicao = df_matches['tipo_torneio'] == 'Copa do Mundo'
df_matches_copadomundo = df_matches[condicao]


# %%
df_qtd_win_times = df_matches[df_matches['time_ganhador'] != 'Empate'].groupby(['time_ganhador']).agg({

    'date': 'count',

}).reset_index()

df_qtd_win_times.sort_values(by='date', ascending=False, inplace=True)
df_top10_times_win = df_qtd_win_times.head(10)
# %%
import plotly.express as px


fig = px.bar(
            df_top10_times_win, 
            x='time_ganhador', 
            y='date',
            color='time_ganhador',
            title='Os 10 times que mais venceram partidas na Copa do Mundo',
            labels={
                    'value': 'Número de Vitórias',
                    'variable': 'Tipo de Jogo',
                    'time_ganhador': 'Times',
                    'date': 'N° de Vitórias'
                    })
fig.show()