from utils import load_ch_neighbours
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = load_ch_neighbours(anim=True)
dates = data[1]['date']

for i in range(len(data)):
    data[i] = np.asarray(data[i]['total_cases'])
    data[i] = np.pad(data[i], (96-len(data[i]), 0), 'constant', constant_values=(0, 0))
x = np.arange(0,len(dates),1)
y = data


def plot(x, y, index):
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title('Total confirmed COVID-19 cases in Switzerland and its neighbours')
    ax.set_xlim(0,len(x)+5)
    ax.set_xticks([4, 35, 65, 96])
    ax.set_xticklabels(['Feb 1', 'Mar 1', 'Apr 1', 'May 1'], fontsize=10)
    ax.set_ylabel('Total confirmed cases', fontsize=10)
    for i in range(len(y)):
        ax.plot(x[0:index+1],y[i][0:index+1])

    plt.savefig('animation/anim%d.png' % (index), dpi=50)
    plt.clf()

for i in range(len(x)):
    plot(x,y,i)




