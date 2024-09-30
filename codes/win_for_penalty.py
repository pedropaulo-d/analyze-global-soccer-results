# %%

import pandas as pd

df_penalty = pd.read_csv('../data/Penalty_Shootouts.csv', sep=',')
df_penalty

# %%

df_best_team_penalty = (df_penalty.groupby(['winner'])
                .agg(
                    qtd_winner_penaltys=('date', 'count')
                    )
                .reset_index())

df_best_team_penalty.sort_values(by='qtd_winner_penaltys', ascending=False, inplace=True)

total_winner = df_best_team_penalty['qtd_winner_penaltys'].sum()

df_best_team_penalty['proporcao'] = df_best_team_penalty['qtd_winner_penaltys'] / total_winner

df_best_team_penalty['proporcao_percentual'] = df_best_team_penalty['proporcao'] * 100

df_10_best_team_penalty = df_best_team_penalty.head(10)

df_10_best_team_penalty
# %%
df_best_team_first_penalty = (df_penalty.groupby(['winner', 'first_shooter'])
                .agg(
                    qtd_winner_penaltys=('date', 'count')
                    )
                .reset_index())

df_best_team_first_penalty.sort_values(by='qtd_winner_penaltys', ascending=False, inplace=True)

total_penaltys = df_best_team_first_penalty['qtd_winner_penaltys'].sum()

df_best_team_first_penalty['proporcao'] = df_best_team_first_penalty['qtd_winner_penaltys'] / total_penaltys

df_best_team_first_penalty['proporcao_percentual'] = df_best_team_first_penalty['proporcao'] * 100

df_10_best_team_first_penalty = df_best_team_first_penalty.head(10)

df_10_best_team_first_penalty

# %%

import plotly.express as px

fig1 = px.bar(df_10_best_team_penalty, 
             x='winner', 
             y='proporcao_percentual',
             color='winner', 
             title='Distribuição de Vitórias por Penaltis',
             labels={
                 'winner': 'Times',
                 'proporcao_percentual': 'Proporção de Vitórias (%)'
             },
             text='proporcao_percentual'
             )

fig1.update_traces(texttemplate='%{text:.2f}%', textposition='outside')

# Exibindo o gráfico
fig1.show()
# %%

fig2 = px.bar(df_10_best_team_first_penalty, 
             x='winner', 
             y='proporcao_percentual',
             color='winner', 
             title='Distribuição de Vitórias por Penaltis (Primeiro Cobrador)',
             labels={
                 'winner': 'Times',
                 'proporcao_percentual': 'Proporção de Vitórias (%)'
             },
             text='proporcao_percentual'
             )

fig2.update_traces(texttemplate='%{text:.2f}%', textposition='outside')

# Exibindo o gráfico
fig2.show()

# South Korea, Argentina
# %%
html_string = fig1.to_html(full_html=True, include_plotlyjs='cdn')
with open("10_best_team_penalty.html", "w") as f:
    f.write(html_string)
# %%

html_string = fig2.to_html(full_html=True, include_plotlyjs='cdn')
with open("10_best_team_first_penalty.html", "w") as f:
    f.write(html_string)
# %%
