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
condicao = df_matches['tournament'] == 'UEFA Euro'
df_matches_eurocopa = df_matches[condicao]

df_matches_eurocopa
# %%
df_qtd_win_times = df_matches_eurocopa[df_matches_eurocopa['time_ganhador'] != 'Empate'].groupby(['time_ganhador']).agg({

    'date': 'count',

}).reset_index()

df_qtd_win_times.sort_values(by='date', ascending=False, inplace=True)
df_top10_times_win = df_qtd_win_times.head(10)
df_top10_times_win
# %%
import plotly.express as px


fig = px.bar(
            df_top10_times_win, 
            x='time_ganhador', 
            y='date',
            color='time_ganhador',
            title='Os 10 times que mais venceram partidas na Euro Copa',
            labels={
                    'value': 'Número de Vitórias',
                    'variable': 'Tipo de Jogo',
                    'time_ganhador': 'Times',
                    'date': 'N° de Vitórias'
                    })
fig.show()
# %%
html_string = fig.to_html(full_html=True, include_plotlyjs='cdn')
with open("10_times_mais_fortes", "w") as f:
    f.write(html_string)
    
# %%
condicao = df_matches['tournament'] == 'Copa América'
df_matches_copaamerica = df_matches[condicao]

df_matches_copaamerica
# %%
df_qtd_win_times = df_matches_copaamerica[df_matches_copaamerica['time_ganhador'] != 'Empate'].groupby(['time_ganhador']).agg({

    'date': 'count',

}).reset_index()

df_qtd_win_times.sort_values(by='date', ascending=False, inplace=True)
df_top10_times_win = df_qtd_win_times.head(10)
df_top10_times_win
# %%

fig2 = px.bar(
            df_top10_times_win, 
            x='time_ganhador', 
            y='date',
            color='time_ganhador',
            title='Os 10 times que mais venceram partidas na Euro Copa',
            labels={
                    'value': 'Número de Vitórias',
                    'variable': 'Tipo de Jogo',
                    'time_ganhador': 'Times',
                    'date': 'N° de Vitórias'
                    })
fig2.show()
# %%

condicao = df_matches['tournament'] == 'Friendly'
df_matches_amistoso = df_matches[condicao]

df_matches_amistoso
# %%
df_qtd_win_times = df_matches_amistoso[df_matches_amistoso['time_ganhador'] != 'Empate'].groupby(['time_ganhador']).agg({

    'date': 'count',

}).reset_index()

df_qtd_win_times.sort_values(by='date', ascending=False, inplace=True)
df_top10_times_win = df_qtd_win_times.head(10)
df_top10_times_win
# %%

fig3 = px.bar(
            df_top10_times_win, 
            x='time_ganhador', 
            y='date',
            color='time_ganhador',
            title='Os 10 times que mais venceram partidas na Euro Copa',
            labels={
                    'value': 'Número de Vitórias',
                    'variable': 'Tipo de Jogo',
                    'time_ganhador': 'Times',
                    'date': 'N° de Vitórias'
                    })
fig3.show()
# %%
