import plotly.express as px
import pandas as pd

df = pd.read_csv('che.csv')[['date', 'new_cases']]
df.columns = ['Date', 'new_cases']
growth = [0]
for i in range (1,len(df['new_cases'])):
    if df['new_cases'][i-1] == 0:
        growth.append(df['new_cases'][i] / df['new_cases'][i-2])
    else:
        growth.append(df['new_cases'][i]/df['new_cases'][i-1])

df['Growth factor'] = growth

fig = px.bar(df, x='Date', y='Growth factor')

fig.update_layout(
    title='Growth factor of epidemic in Switzeralnd (new cases/new cases on the previous day)',
    autosize=False,
    width=900,
    height=400,
    xaxis=dict(tickangle=45)
)

fig.write_html('plotly_growth.html', include_plotlyjs='cdn')