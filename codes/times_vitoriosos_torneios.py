# %%

import pandas as pd
import plotly.express as px
# %%

df_matchs = pd.read_csv('../data/Match_Results.csv', sep=',')
df_matchs
# %%
def tipo_vitoria(row):
    if row['home_score'] > row['away_score']:  # Vitória do time da casa
        return row['away_team']
        
    elif row['home_score'] < row['away_score']:  # Vitória do time visitante
        return row['away_team']
    else:
        return 'Empate'
    
df_matchs['time_ganhador'] = df_matchs.apply(tipo_vitoria, axis=1)

df_matchs
# %%

df_qtd_win_team_tournament = (df_matchs[df_matchs['time_ganhador'] != 'Empate'].groupby(['tournament', 'time_ganhador'])
                .agg(
                    qtd_win=('date', 'count')
                    )
                .reset_index())

df_10_qtd_win_team_tournament = df_qtd_win_team_tournament.sort_values(by='qtd_win', ascending=False).head(10)
df_10_qtd_win_team_tournament
# %%
