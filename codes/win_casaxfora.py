# %%
import pandas as pd

df_matches = pd.read_csv('../data/Match_Results.csv', sep=',')

df_matches
# %%
def tipo_vitoria(row):
    if row['home_score'] > row['away_score']:  # Vitória do time da casa
        if row['neutral']:  # Se foi em campo neutro
            return 'Vitória em Campo Neutro'
        else:
            return 'Vitória em Casa'
    elif row['home_score'] < row['away_score']:  # Vitória do time visitante
        if row['neutral']:  # Se foi em campo neutro
            return 'Vitória em Campo Neutro'
        else:
            return 'Vitória Fora de Casa'
    else:
        return 'Empate'
    
df_matches['tipo_vitoria'] = df_matches.apply(tipo_vitoria, axis=1)

df_matches
# %%
df_qtd_win = df_matches.groupby(['tipo_vitoria']).agg({

    'date': 'count',

}).reset_index()

# %%
import plotly.express as px

fig = px.bar(
            df_qtd_win, 
            x='tipo_vitoria', 
            y='date',
            color='tipo_vitoria',
            title='Análise de Vitórias em Casa vs Fora',
            labels={
                    'value': 'Número de Vitórias',
                    'variable': 'Tipo de Jogo',
                    'date': 'N° de Vitórias',
                    'tipo_vitoria': 'Tipo de Vitória'
                    },
            text='date'
            )

fig.update_traces(texttemplate='%{text}', textposition='outside')

fig.show()
# %%
html_string = fig.to_html(full_html=True, include_plotlyjs='cdn')
with open("vitorias_em_casa_vs_fora.html", "w") as f:
    f.write(html_string)
# %%
