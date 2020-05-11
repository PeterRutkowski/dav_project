import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('che.csv')
dates = data['date']
data = data[['new_cases', 'new_deaths']]
x = np.asarray(data['new_cases'])
throwback = 30

# SimpleExpSmoothing
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
model = SimpleExpSmoothing(x)
model_fit = model.fit(smoothing_level=0.6, optimized=True)
pred = model_fit.predict(len(x), len(x)+throwback-1)

sns.set(style="whitegrid")
fig, ax = plt.subplots()
ax.bar(np.arange(0,len(x),1), x, color=(128/255,170/255,255/255))
ax.bar(np.arange(len(x),len(x)+throwback,1), pred, color=(255/255,51/255,51/255))
ax.set_title('Predicted evolution of new daily COVID-19 cases\n'
             'in Switzerland using SES model', fontsize=12)
ax.set_ylabel('New daily cases', fontsize=10)
ax.set_yticks(np.arange(0,1500,200))
ax.set_yticklabels([x for x in np.arange(0,1500,200)], fontsize=10)
ax.set_xticks([4,35,65,96])
ax.set_xticklabels(['Mar 1', 'Apr 1', 'May 1', 'Jun 1'], fontsize=10)
ax.grid(axis='x')

lgd = ax.legend(fontsize=10, frameon=True, loc=(0.65,0.83))

def add_patches(legend):
    from matplotlib.patches import Patch

    handles, labels = [], []
    handles.append(Patch(facecolor=(128/255,170/255,255/255), edgecolor=(128/255,170/255,255/255)))
    handles.append(Patch(facecolor=(255/255,51/255,51/255), edgecolor=(255/255,51/255,51/255)))
    labels.append('Confirmed cases')
    labels.append('Prediction')

    legend._legend_box = None
    legend._init_legend_box(handles, labels)
    legend._set_loc(legend._loc)
    legend.set_title(legend.get_title().get_text())

add_patches(lgd)

plt.text(1, -0.12, 'Source: ourworldindata.org',
         horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, size=7)

plt.savefig('prediction_smoothing_cases.png', dpi=400)