import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

countries = ['aut','che','fra','ger','ita','lie']
data = []
for country in countries:
    country_data = pd.read_csv('%s.csv'%(country))
    data.append(np.asarray(country_data[['total_deaths']]))
    if country == 'fra':
        dates = np.asarray(country_data[['date']])
        dates = np.squeeze(dates, axis=1)
data = np.asarray(data)

for i in range(len(data)):
    data[i] = np.squeeze(data[i], axis=1)

data[0] = np.pad(data[0], (32, 0), 'constant', constant_values=(0, 0))
data[1] = np.pad(data[1], (32, 0), 'constant', constant_values=(0, 0))
data[3] = np.pad(data[3], (3, 0), 'constant', constant_values=(0, 0))
data[4] = np.pad(data[4], (6, 0), 'constant', constant_values=(0, 0))
data[5] = np.pad(data[5], (46, 0), 'constant', constant_values=(0, 0))

for i in range(len(data)):
    data[i] = data[i][35:]

data = np.asarray(data)
x = np.arange(0,61,1)

data_preproc = pd.DataFrame({
    'Date': x,
    'AUT': data[0],
    'CHE': data[1],
    'FRA': data[2],
    'GER': data[3],
    'ITA': data[4],
    'LIE': data[5]})

sns.set(style="whitegrid")

fig, ax = plt.subplots()

plot = sns.lineplot(x = 'Date', y = 'value', hue='Country',
                    data=pd.melt(data_preproc, ['Date'], var_name='Country'))
plot.set(title='Total number of COVID-19 fatalities in Switzerland\nand neighbouring countries',
         ylabel='Total number of COVID-19 fatalities [thousands]', yticks=np.arange(0,26000,5000),
         yticklabels = np.arange(0,26,5), xticks=np.arange(0,70,10),
         xticklabels=[dates[i] for i in range(35,35+70,10)])

plot = ax.get_figure()
fig.savefig('total_deaths_neighbours.png')