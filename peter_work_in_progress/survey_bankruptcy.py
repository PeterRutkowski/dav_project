import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('survey_bankruptcy.csv')

sns.set(style="whitegrid")

ax = sns.barplot(x="label", y="val", data=data, color=(128/255,170/255,255/255))
ax.set_title('In your opinion, how high is the likelihood of bankruptcy?', fontsize=12)
ax.set_xlabel('')
ax.set_xticklabels([el for el in data['label']], size=7)
ax.set_ylabel('Likelihood of bankruptcy', fontsize=9)
ax.set_yticks(np.arange(0,60,10))
ax.set_yticklabels([str(el)+'%' for el in np.arange(0,60,10)], size = 9)



for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 1, str(int(height))+'%',
            ha="center", size=9)

plt.text(0.94, -0.11, 'Source: Schweiz Tourismus; FH Westschweiz Wallis,\n'
                      'Wirtschaftliche Auswirkungen der Coronavirus-Krise\n'
                      'auf den Schweizer Tourismus 2020, page 62',
         horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, size=5)

plt.text(0.65, -0.101, 'Details: March 23-24, 2020;\n2046 establishments',
         horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, size=5)


plt.savefig('survey_bankruptcy.png', dpi=400)

