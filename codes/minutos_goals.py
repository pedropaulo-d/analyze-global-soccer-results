# %%
import pandas as pd

df_goal = pd.read_csv('../data/Goal_Scorers.csv', sep=',')
df_goal
# %%
# Usando pd.cut para categorizar os minutos em faixas de tempo
df_goal['time_interval'] = pd.cut(df_goal['minute'], 
                             bins=[0, 15, 30, 45, 60, 75, 90, 105, 120, 135],  # Definindo os intervalos
                             labels=['0-15', '16-30', '31-45', '46-60', '61-75', '76-90', '91-105', '106-120', '135+'],  # Nomeando os intervalos
                             right=False)  # right=False significa que o limite superior é exclusivo

df_goal
# %%
df_goal_minute = df_goal.groupby(['time_interval']).agg({

    'date': 'count',

}).rename(columns={

    'date': 'qtd_gols',

}).reset_index()

df_goal_minute
# %%
# Calcular o total de gols
total_gols = df_goal_minute['qtd_gols'].sum()

# Calcular a proporção de gols em cada intervalo
df_goal_minute['proporcao'] = df_goal_minute['qtd_gols'] / total_gols

# Em percentual
df_goal_minute['proporcao_percentual'] = df_goal_minute['proporcao'] * 100

df_goal_minute
# %%
import plotly.express as px

fig = px.bar(df_goal_minute, 
             x='time_interval', 
             y='proporcao_percentual',
             color='time_interval', 
             title='Distribuição de Gols por Intervalo de Tempo',
             labels={
                 'time_interval': 'Intervalo de Tempo (minutos)',
                 'proporcao_percentual': 'Proporção de Gols (%)'
             },
             text='proporcao_percentual'
             )

fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')

# Exibindo o gráfico
fig.show()
# %%
html_string = fig.to_html(full_html=True, include_plotlyjs='cdn')
with open("distribuicaodegols.html", "w") as f:
    f.write(html_string)
# %%
