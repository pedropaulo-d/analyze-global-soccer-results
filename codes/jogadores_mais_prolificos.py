# %%

import pandas as pd

df_matches = pd.read_csv('../data/Goal_Scorers.csv', sep=',')

df_matches
# %%
df_qtd_goals = df_matches.groupby(['scorer']).agg({

    'date': 'count',

}).reset_index()

df_qtd_goals.sort_values(by='date', ascending=False, inplace=True)
df_10Players_goals = df_qtd_goals.head(10)
df_10Players_goals


# %%
# Jogadores com mais gols nos torneios da FIFA.
import plotly.express as px


fig1 = px.bar(
            df_10Players_goals, 
            x='scorer', 
            y='date',
            color='scorer',
            title='Os 10 Jogadores com Mais Gols nos Torneios da FIFA',
            labels={
                    'value': 'Número de Vitórias',
                    'variable': 'Tipo de Jogo',
                    'scorer': 'Jogadores',
                    'date': 'N° de Gols'},
            text='date'
            )

fig1.update_traces(texttemplate='%{text}', textposition='outside')
fig1.show()

  
# %%
df_matches.head()
# %%

df_top_scorers = df_matches.groupby(['team', 'scorer']).size().reset_index(name='gols')
df_top_scorers = df_top_scorers.sort_values(by='gols', ascending=False)
df_top_scorers

# %%

top_scorers_by_team = df_top_scorers.groupby('team').first().reset_index()
top_scorers_by_team = top_scorers_by_team.sort_values(by='gols', ascending=False)
top10_scorers_by_team = top_scorers_by_team.head(10)

# %%
# Jogadores com mais gols por time nos torneios da FIFA.

fig2 = px.bar(
    top10_scorers_by_team, 
    x='team', 
    y='gols', 
    color='scorer', 
    title='Top Artilheiros por Time',
    labels={'gols': 'Quantidade de Gols', 'team': 'Time', 'scorer': 'Artilheiro'}
)
fig2.show()
