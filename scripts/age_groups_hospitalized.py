import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
fp='C:/Users/rysza/Desktop/python data analysis/Project/COVID19_Fallzahlen_Kanton_TG_Geschlecht_Alterskategorie.csv'

xls = pd.ExcelFile('C:/Users/rysza/Desktop/python data analysis/Project/agegroups.xlsx')

df = pd.read_excel(xls, 'COVID19 Altersverteilung Hospit',header=6)

df=df[['Altersklasse','Total hospitalisiert: Anzahl']]
df=df.rename(columns={'Altersklasse':'agegroup','Total hospitalisiert: Anzahl':'hospitalized'})
df=df[:9]

g=sns.barplot(x='agegroup',y='hospitalized',data=df,color='blue')
sns.set_style("whitegrid")

for index, row in df.iterrows():
    g.text(index,row.hospitalized+20, round(row.hospitalized), color='black', ha="center")

labels=[]
for i in df['agegroup']:
    labels.append(i+' years')
g.set_xticklabels(labels ,rotation=35,ha='right')
plt.xlabel('')
plt.ylabel('')
plt.yticks(ticks=[0,250,500,750,1000,1250,1500],labels=['0','250','500','750','1000','1250','1500'])
axes = plt.gca()
axes.set_ylim([0,1500])
plt.title('Hospitalizations due to the COVID-19 in Switzerland by age group',loc='left')
plt.tight_layout()
fig=g.get_figure()
fig.savefig('C:/Users/rysza/Desktop/python data analysis/Project/plots/Hospitalizations_due_to_the_COVID-19_in_Switzerland_by_age_group.png')