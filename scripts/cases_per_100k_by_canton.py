import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
fp='C:\\Users\\rysza\\Desktop\\python data analysis\zajecia7\map switzerland\\swisscanton\\ch-cantons.shp'
map_df = gpd.read_file(fp)
map_df.plot()
map_df['Canton']=['AG','AR','AI','BL','BS','BE','FR','GE','GL','GR','JU','LU','NE','NW','OW','SG','SH','SZ','SO','TG','TI','UR','VS','VD','ZG','ZH']
xls = pd.ExcelFile('C:/Users/rysza/Desktop/python data analysis/Project/agegroups.xlsx')

df = pd.read_excel(xls, 'COVID19 Kantone',header=6)
df=df[['Kanton','Inzidenz/100 000']].rename(columns={'Kanton':'Canton','Inzidenz/100 000':'cases'})

merged = map_df.set_index('Canton').join(df.set_index('Canton'))

variable = 'cases'
vmin, vmax = 92.7, 1031.1

fig, ax = plt.subplots(1, figsize=(10, 6))

merged.plot(column=variable, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.5')
ax.axis('off')
ax.set_title('Cases per 100k inhabitants', fontdict={'fontsize': '10', 'fontweight' : '3'})
ax.annotate('Source: Bundesamt für Gesundheit ',xy=(0.1, .08),
            xycoords='figure fraction', horizontalalignment='left',
            verticalalignment='top', fontsize=8, color='#555555')
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
fig.set_size_inches(7,3)
fig.savefig('C:\\Users\\rysza\\Desktop\\python data analysis\\Project\\plots\\cases_per_100k_by_cantons.png', dpi=300)
