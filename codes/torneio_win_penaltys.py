# %%

import pandas as pd
import plotly.express as px

# %%

df_penalty = pd.read_csv('../data/Penalty_Shootouts.csv', sep=',')
df_penalty

# %%
df_matches = pd.read_csv('../data/Match_Results.csv', sep=',')
df_matches

# %%

df_match_penalty = pd.merge(df_matches, df_penalty, on=['date', 'home_team', 'away_team'])

df_match_penalty
# %%

df_best_tournament_penalty = (df_match_penalty.groupby(['tournament'])
                .agg(
                    qtd_winner=('winner', 'count')
                    )
                .reset_index())

df_best_tournament_penalty.sort_values(by='qtd_winner', ascending=False, inplace=True)



total_qtd_winner = df_best_tournament_penalty['qtd_winner'].sum()

df_best_tournament_penalty['proporcao'] = df_best_tournament_penalty['qtd_winner'] / total_qtd_winner

df_best_tournament_penalty['proporcao_percentual'] = df_best_tournament_penalty['proporcao'] * 100

df_10_best_team_penalty = df_best_tournament_penalty.head(10)

df_10_best_team_penalty

# %%


fig1 = px.bar(df_10_best_team_penalty, 
             x='tournament', 
             y='proporcao_percentual',
             color='tournament', 
             title='Distribuição de Vitórias por Penaltis por Torneios',
             labels={
                 'tournament': 'Torneios',
                 'proporcao_percentual': 'Proporção de Vitórias (%)'
             },
             text='proporcao_percentual'
             )

fig1.update_traces(texttemplate='%{text:.2f}%', textposition='outside')

# Exibindo o gráfico
fig1.show()
# %%

html_string = fig1.to_html(full_html=True, include_plotlyjs='cdn')
with open("df_10_best_team_penalty.html", "w") as f:
    f.write(html_string)

# %%
