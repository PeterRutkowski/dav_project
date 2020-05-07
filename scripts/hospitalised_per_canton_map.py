import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
fp='C:\\Users\\rysza\\Desktop\\python data analysis\zajecia7\map switzerland\\swisscanton\\ch-cantons.shp'
map_df = gpd.read_file(fp)
map_df.plot()
map_df['Canton']=['AG','AR','AI','BL','BS','BE','FR','GE','GL','GR','JU','LU','NE','NW','OW','SG','SH','SZ','SO','TG','TI','UR','VS','VD','ZG','ZH']
df = pd.read_csv('C:/Users/rysza/Desktop/python data analysis/Project/covid19_hospitalized_switzerland_openzh.csv', header=0)

df=df.loc[df['Date'] == '2020-04-28']
df=df.drop(['Date'],axis=1).T.reset_index()
df=df.rename(columns={'index':'Canton',63:'hospitalized'})
df['hospitalized'] = df['hospitalized'].fillna(0)
merged = map_df.set_index('Canton').join(df.set_index('Canton'))

variable = 'hospitalized'
vmin, vmax = 0, 1200

fig, ax = plt.subplots(1, figsize=(10, 6))

merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.5')
ax.axis('off')
ax.set_title('Hospitalized by cantons', fontdict={'fontsize': '10', 'fontweight' : '3'})
ax.annotate('Source: Kaggle COVID19 Hospitalized Switzerland',xy=(0.1, .08),
            xycoords='figure fraction', horizontalalignment='left',
            verticalalignment='top', fontsize=8, color='#555555')
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
fig.set_size_inches(7,3)
fig.savefig('C:\\Users\\rysza\\Desktop\\python data analysis\\Project\\plots\\hospitalized_by_canton_map.png', dpi=300)