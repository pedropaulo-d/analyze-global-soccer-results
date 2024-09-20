# %%
import pandas as pd

df_match = pd.read_csv('../data/Match_Results.csv', sep=',')
df_match

# %%
df_match['date'] = pd.to_datetime(df_match['date']).dt.year
df_match = df_match[df_match['date'] <= 2023]
# %%
df_match.dtypes
# %%
df_jogos_ano = df_match.rename(columns={

    'date': 'Ano',
    'tournament': 'Jogos'

}).groupby(['Ano']).agg({

    'Jogos': 'count',

}).reset_index()

# %%
import plotly.express as px

df_jogos_ano['Jogos_Media'] = df_jogos_ano['Jogos'].rolling(window=5).mean()

fig = px.line(df_jogos_ano, x='Ano', y=['Jogos', 'Jogos_Media'], 
              title='Quantidade de Jogos por Ano (com Tendência)',
              labels={'value': 'Número de Jogos',
                      'variable': 'Tipo de Métrica'})
fig.show()

# %%
