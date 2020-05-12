from utils import load_ch_neighbours
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = load_ch_neighbours(anim=True)
dates = data[1]['date']

for i in range(len(data)):
    data[i] = np.asarray(data[i]['new_cases'])
    data[i] = np.pad(data[i], (96-len(data[i]), 0), 'constant', constant_values=(0, 0))
x = np.arange(0,len(dates),1)
y = data[0]


def plot(x, y, index):
    sns.set(style="whitegrid")
    x = x[0:index+1]
    y = y[0:index+1]
    fig, ax = plt.subplots()
    ax.plot(x,y)

for i in range(len(x)):
    plot(x,y,i)
    plt.savefig('animation/anim%d.png'%(i), dpi=400)
    plt.clf()





