import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from  utils import drop_prepandemic_dates, save_ch_neighbours
save_ch_neighbours()

data = pd.read_csv('che.csv')
data = data[['date','new_cases']]

data = drop_prepandemic_dates(data)
dates = data['date']


sns.set(style="whitegrid")

fig, ax = plt.subplots()
plot = sns.barplot(x='date', y='new_cases', data=data, ax=ax)
plot.set(xticks=np.arange(0,len(data['date']),15), xticklabels=[dates[ind] for ind in range(0,len(data['date']),15)],
         xlabel='Date', ylabel='New daily cases', title='New daily cases of COVID-19 in Switzerland')

plot = ax.get_figure()
fig.savefig('new_daily_cases.png')
