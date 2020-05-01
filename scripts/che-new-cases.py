import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from  utils import drop_prepandemic_dates


data = pd.read_csv('switzerland.csv')
data = data[['date','new_cases']]

data = drop_prepandemic_dates(data)

sns.set(style="whitegrid")

fig, ax = plt.subplots()

xticks = np.arange(0,64,10)
dates = []
for index, row in data.iterrows():
    print(index)
    if (index-59) in xticks:
        dates.append(row['date'])
print(dates)

plot = sns.barplot(x='date', y='new_cases', data=data, ax=ax)
plot.set(xticks=xticks, xticklabels=['28Feb','9Mar','19Mar','29Mar','8Apr','18Apr','28Apr'],
         xlabel='Date', ylabel='New daily cases', title='New daily cases of COVID-19 in Switzerland')

plot = ax.get_figure()
fig.savefig('trial.png')