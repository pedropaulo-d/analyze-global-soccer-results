# %%
import pandas as pd

df_goal = pd.read_csv('../data/Goal_Scorers.csv', sep=',')
df_match = pd.read_csv('../data/Match_Results.csv', sep=',')


# %%
df_goal['date'] = pd.to_datetime(df_goal['date']).dt.year
df_goal = df_goal[df_goal['date'] <= 2023]

df_match['date'] = pd.to_datetime(df_match['date']).dt.year
df_match = df_match[df_match['date'] <= 2023]

# %%
df_match

# %%
df_goal
# %%
df_gols_ano = df_goal.groupby(['date']).agg({'scorer': 'count'}).reset_index()
df_gols_ano
# %%
df_jogos_ano = (df_match.groupby(['date'])
                .agg({'tournament': 'count'})
                .rename(columns={'tournament': 'Jogos'})
                .reset_index())

df_jogos_ano
# %%
df_media_gols_jogos = pd.merge(df_gols_ano, df_jogos_ano, left_on='date', right_on='date')

df_media_gols_jogos
# %%

df_media_gols_jogos['media_gols_jogo'] = df_media_gols_jogos['scorer'] / df_media_gols_jogos['Jogos']

# %%
df_media_gols_jogos.head()

# %%
import plotly.express as px

fig = px.line(df_media_gols_jogos, x='date', y='media_gols_jogo', 
              title='Média de Gols por Jogos no Ano',
              labels={
                  
                  'media_gols_jogo': 'Média dos gols por jogos',
                  'date': 'Ano'
                  
                  })
fig.show()
