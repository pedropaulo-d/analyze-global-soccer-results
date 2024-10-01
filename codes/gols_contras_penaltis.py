# %%
import pandas as pd

df_goal = pd.read_csv('../data/Goal_Scorers.csv', sep=',')
df_goal
# %%

df_goal['date'] = pd.to_datetime(df_goal['date']).dt.year
df_goal
# %%

df_qtd_gols_contras = (df_goal.groupby(['date'])
                .agg(
                    qtd_gol_contra=('own_goal', 'sum')
                    )
                .reset_index())

df_qtd_gols_contras
# %%

import plotly.express as px


fig = px.line(df_qtd_gols_contras, x='date', y='qtd_gol_contra', 
              title='Quantidade total de gols contra por Ano',
              labels={
                  
                  'qtd_gol_contra': 'Total de gols contra',
                  'date': 'Ano',
                  'value': 'Total de gols',
                  'variable':'Tipo de Métrica'
                  
                  })
fig.show()

# %%
df_penalty = pd.read_csv('../data/Goal_Scorers.csv', sep=',')
df_penalty
# %%

df_penalty['date'] = pd.to_datetime(df_penalty['date']).dt.year
df_penalty
# %%

df_qtd_gols_penaltis = (df_penalty.groupby(['date'])
                .agg(
                    qtd_gol_penaltis=('penalty', 'sum')
                    )
                .reset_index())

df_qtd_gols_penaltis
# %%

fig = px.line(df_qtd_gols_penaltis, x='date', y='qtd_gol_penaltis', 
              title='Quantidade total de gols de Penaltis por ano',
              labels={
                  
                  'qtd_gol_penaltis': 'Total de gols de Penaltis',
                  'date': 'Ano',
                  'value': 'Total de Gols',
                  'variable':'Tipo de Métrica'
                  
                  })
fig.show()
# %%

df_gols_penaltis_contra = pd.merge(df_qtd_gols_contras, df_qtd_gols_penaltis, left_on='date', right_on='date')
df_gols_penaltis_contra.rename(columns={'qtd_gol_contra': 'Gols Contra', 'qtd_gol_penaltis': 'Gols de Penaltis'}, inplace=True)
# %%

fig = px.line(df_gols_penaltis_contra, x='date', y=['Gols de Penaltis', 'Gols Contra'], 
              title='Quantidade total de gols de Penaltis e Contra por ano',
              labels={
                  
                  'qtd_gol_penaltis': 'Total de gols de Penaltis e Contra',
                  'date': 'Ano',
                  'value': 'Total de Gols',
                  'variable':'Tipo de Métrica',
                 
                  })
fig.show()
# %%
