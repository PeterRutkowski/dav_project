import plotly.express as px
import pandas as pd

df = pd.read_csv('che.csv')[['date', 'total_cases']]
df.columns = ['Date', 'Total number of cases']

fig = px.line(df, x='Date', y='Total number of cases')

fig.update_layout(
    title='Total number of COVID-19 cases in Switzerland',
    autosize=False,
    width=900,
    height=400,
    xaxis=dict(tickangle=45)
)

fig.write_html('plotly_cases.html', include_plotlyjs='cdn')