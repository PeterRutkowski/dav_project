import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.patches as mpatches
fp='C:/Users/rysza/Desktop/python data analysis/Project/COVID19_Fallzahlen_Kanton_TG_Geschlecht_Alterskategorie.csv'

xls = pd.ExcelFile('C:/Users/rysza/Desktop/python data analysis/Project/agegroups.xlsx')

df1 = pd.read_excel(xls, 'COVID19 Altersverteilung Hospit',header=6)

df1=df1[['Altersklasse','Total hospitalisiert: Anzahl']]
df1=df1.rename(columns={'Altersklasse':'agegroup','Total hospitalisiert: Anzahl':'hospitalized'})
df1=df1[:9]

df2=pd.read_excel(xls, 'COVID19 Altersverteilung TodF',header=6)
df2=df2[['Altersklasse','Total Todesfälle: Anzahl']]
df2=df2.rename(columns={'Altersklasse':'agegroup','Total Todesfälle: Anzahl':'deaths'})
df2=df2[:9]
df1['deaths']=df2['deaths'] 

sns.set_style("whitegrid")
g=sns.barplot(x='agegroup',y='hospitalized',data=df1,color="#80aaff")
sns.barplot(x='agegroup',y='deaths',data=df1,color='#ff3333')
sns.set_style("whitegrid")

for index, row in df1.iterrows():
    g.text(index,row.hospitalized+20, round(row.hospitalized), color='black', ha="center",fontsize=9)

labels=[]
for i in df1['agegroup']:
    labels.append(i+' years')
g.set_xticklabels(labels ,rotation=35,ha='right',fontsize=10)
plt.xlabel('')
plt.ylabel('')
plt.yticks(ticks=[0,250,500,750,1000],labels=['0','250','500','750','1000'])
axes = plt.gca()
axes.set_ylim([0,1300])
plt.title('Hospitalizations due to the COVID-19 in Switzerland by age group',loc='left',fontsize=12)
red_patch = mpatches.Patch(color='#ff3333', label='deaths')
blue_patch = mpatches.Patch(color="#80aaff", label='hospitalizations')
plt.legend(handles=[blue_patch,red_patch],loc='upper left',frameon=False)
plt.tight_layout()
plt.annotate('Source: Bundesamt für Gesundheit',xy=(1,0.03),
            xycoords='figure fraction', horizontalalignment='right',
            verticalalignment='top', fontsize=7, color='#555555')
fig=g.get_figure()
fig.savefig('C:/Users/rysza/Desktop/python data analysis/Project/plots/Hospitalizations_due_to_the_COVID-19_in_Switzerland_by_age_group.png',dpi=400)
