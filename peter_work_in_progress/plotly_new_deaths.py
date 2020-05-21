import plotly.express as px
import pandas as pd

df = pd.read_csv('che.csv')[['date', 'new_deaths']]
df.columns = ['Date', 'Number of new daily deaths']

fig = px.bar(df, x='Date', y='Number of new daily deaths')

fig.update_layout(
    title='Number of new daily COVID-19 deaths in Switzerland',
    autosize=False,
    width=900,
    height=400,
    xaxis=dict(tickangle=45)
)

fig.write_html('plotly_new_deaths.html', include_plotlyjs='cdn')