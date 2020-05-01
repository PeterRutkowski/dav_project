import pandas as pd
import seaborn as sns


data = pd.read_csv('switzerland.csv')
data = data[['date','new_cases']]


sns.set(style="whitegrid")

ax = sns.barplot(x='date', y='new_cases', data=data)

fig = ax.get_figure()
fig.savefig('trial.png')