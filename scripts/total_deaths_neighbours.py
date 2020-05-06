import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

countries = ['aut','che','fra','ger','ita','lie']
data = []
for country in countries:
    country_data = pd.read_csv('%s.csv'%(country))
    data.append(np.asarray(country_data[['total_deaths']]))
data = np.asarray(data)

for i in range(len(data)):
    data[i] = np.squeeze(data[i], axis=1)

data[0] = np.pad(data[0], (32, 0), 'constant', constant_values=(0, 0))
data[1] = np.pad(data[1], (32, 0), 'constant', constant_values=(0, 0))
data[3] = np.pad(data[3], (3, 0), 'constant', constant_values=(0, 0))
data[4] = np.pad(data[4], (6, 0), 'constant', constant_values=(0, 0))
data[5] = np.pad(data[5], (46, 0), 'constant', constant_values=(0, 0))

data = np.asarray(data)
x = np.arange(0,96,1)

data_preproc = pd.DataFrame({
    'Year': x,
    'AUT': data[0],
    'CHE': data[1],
    'FRA': data[2],
    'GER': data[3],
    'ITA': data[4],
    'LIE': data[5]})

sns.set(style="whitegrid")

fig, ax = plt.subplots()

plot = sns.lineplot(x = 'Year', y = 'value', hue='variable', data=pd.melt(data_preproc, ['Year']))
plot.set(title='Total fatalities of COVID-19')

plot = ax.get_figure()
fig.savefig('total_deaths_neighbours.png')