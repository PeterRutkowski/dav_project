import seaborn as sns
import pandas as pd
from utils import load_ch_neighbours
import matplotlib.pyplot as plt

che, fra, ita, ger, aut, lie = load_ch_neighbours()

total_deaths = [che['total_deaths'], fra['total_deaths'],
                ita['total_deaths'], ger['total_deaths'],
                aut['total_deaths'], lie['total_deaths']]

time = che['date']

total_deaths = pd.concat(total_deaths, axis=1)
total_deaths.columns = ['che','fra','ita','ger','aut','lie']

print(total_deaths.head())

fig, ax = plt.subplots()




sns.lineplot(data=che['total_deaths'], ax=ax)
sns.lineplot(data=fra['total_deaths'], ax=ax)
sns.lineplot(data=ita['total_deaths'], ax=ax)
sns.lineplot(data=ger['total_deaths'], ax=ax)
sns.lineplot(data=aut['total_deaths'], ax=ax)
sns.lineplot(data=lie['total_deaths'], ax=ax)




fig = ax.get_figure()
fig.savefig('trial.png')